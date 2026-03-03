# -*- coding: utf-8 -*-
"""AI-Powered ERP Ticket Triaging System
   LLM-based classification and routing
"""

!pip install -q transformers accelerate bitsandbytes torch

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

model_name = "mistralai/Mistral-7B-Instruct-v0.2"

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4"
)

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=bnb_config,
    device_map="auto"
)

import json

def analyze_ticket(ticket_text):

    prompt = f"""
You are an ERP support ticket triaging assistant.

Analyze the ticket and return ONLY valid JSON.

JSON format:
{{
  "category": "Finance | Inventory | HR | Procurement | IT",
  "erp_platform": "SAP | Oracle Fusion | Microsoft Dynamics | Unknown",
  "issue_type": "Issue | Change Request | Support Request | Information Request",
  "priority": "High | Medium | Low"
}}

Ticket:
{ticket_text}

JSON:
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True).to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
        do_sample=False,
        pad_token_id=tokenizer.eos_token_id
    )

    response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return response_text

def route_ticket(parsed_data):
    category = parsed_data["category"]
    platform = parsed_data["erp_platform"]

    if category == "Finance" and platform == "SAP":
        return "SAP Finance Support Team"
    elif category == "HR":
        return "HR Systems Support Team"
    elif category == "Inventory":
        return "Inventory Operations Team"
    else:
        return "General ERP Support Team"

import re
import json

ticket = input("Enter ERP Support Ticket:\n")

raw_output = analyze_ticket(ticket)

print("\n--- LLM RAW OUTPUT ---")
print(raw_output)

try:
    json_start = raw_output.rfind("{")
    json_end = raw_output.rfind("}") + 1

    if json_start != -1 and json_end != -1:
        json_str = raw_output[json_start:json_end]
        parsed = json.loads(json_str)

        print("\n--- STRUCTURED OUTPUT ---")
        print(json.dumps(parsed, indent=2))

        assigned_team = route_ticket(parsed)

        print("\n--- ROUTING RESULT ---")
        print("Assigned To:", assigned_team)

    else:
        print("⚠ No valid JSON found.")

except Exception as e:
    print("⚠ JSON parsing failed:", e)
