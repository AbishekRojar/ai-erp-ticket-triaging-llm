# AI-erp-ticket-triaging-llm
LLM-powered ERP support ticket triaging system using Mistral 7B
# AI-Powered ERP Ticket Triaging System

## 1. Problem Understanding

ERP support teams receive a large number of unstructured support tickets related to different business modules such as Finance, HR, Inventory, Procurement, and IT.

Currently, tickets are manually:
- Categorized
- Assigned to the correct team
- Prioritized
- Interpreted for issue type
- Responded to with an acknowledgment

This manual triaging process increases response time, operational cost, and may impact SLA compliance.

The goal of this project is to build a Proof of Concept (POC) that uses a Large Language Model (LLM) to automate ticket triaging and improve efficiency.

---

## 2. System Architecture Overview

The system follows this architecture:

User Ticket  
→ Prompt Engineering  
→ Instruction-Tuned LLM (Mistral 7B Instruct)  
→ Structured JSON Output  
→ Backend Parsing & Validation  
→ Routing Logic  
→ Assigned Support Team  

The LLM performs semantic understanding and classification, while backend logic ensures deterministic routing and structured handling.

---

## 3. Model Choice Justification

This POC uses **Mistral 7B Instruct**, an open-source, instruction-tuned transformer model.

Reasons for choosing this model:

- Strong semantic understanding capability
- Instruction-tuned for structured prompt tasks
- Capable of JSON-based structured output
- No dependency on paid API services
- Cost-efficient and suitable for enterprise deployment
- Vendor-neutral and privacy-friendly (can run on controlled infrastructure)

Quantization (4-bit) is used to reduce memory usage and enable efficient inference.

---

## 4. How the System Works

### Step 1 – Ticket Input  
User enters an unstructured ERP support ticket in natural language.

### Step 2 – Prompt Construction  
The ticket is inserted into a structured prompt instructing the model to return valid JSON.

### Step 3 – LLM Classification  
The model returns structured JSON containing:
- category
- erp_platform
- issue_type
- priority

### Step 4 – JSON Parsing  
The system safely extracts the JSON block from model output.

### Step 5 – Routing Logic  
Based on category and ERP platform, the ticket is assigned to the appropriate support team.

---

## 5. Demonstration Example

### Example Input
System performance is very slow during peak hours.


### Example Output

```json
{
  "category": "IT",
  "erp_platform": "Unknown",
  "issue_type": "Support Request",
  "priority": "Medium"
}
```

**Routing Result:**  
Assigned To: General ERP Support Team

## 6. Known Limitations

This implementation is a Proof of Concept (POC) and has the following limitations:

- Does not use historical SLA data or user priority history  
- No confidence scoring mechanism for classification certainty  
- No human-in-the-loop validation for ambiguous tickets  
- Routing logic is rule-based after classification  
- Requires GPU for optimal inference performance  

---

## 7. Scalability & Production Considerations

In a production environment, the system can be enhanced by:

- Deploying the model behind a REST API service  
- Using asynchronous queue-based processing for high ticket volume  
- Adding confidence thresholds for automated vs manual routing  
- Implementing logging, monitoring, and error tracking  
- Fine-tuning the model using historical ERP ticket data  
- Using load balancing for handling large-scale ticket inflow  

---

## 8. Technologies Used

- Python  
- Hugging Face Transformers  
- PyTorch  
- BitsAndBytes (4-bit quantization)  
- Mistral 7B Instruct  

---

## 9. Conclusion

This project demonstrates how Large Language Models can automate ERP ticket triaging by transforming unstructured ticket descriptions into structured, actionable outputs.

The solution aligns with the assessment objectives by showcasing business understanding, structured architecture design, practical feasibility, and scalability awareness.





