# AutoStream

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Add your Gemini API key in:
- agent/intent.py
- agent/rag.py

3. Run:
python app.py

---

## Architecture

This project uses a modular agent design with intent detection, RAG-based knowledge retrieval, and a controlled lead capture workflow.

Intent detection is handled using Gemini, classifying user inputs into greeting, product inquiry, or high intent. Based on intent, the system routes requests to either a retrieval module or a lead collection flow.

The RAG system uses a local JSON knowledge base to ensure accurate and grounded responses. Lead capture is implemented via a structured state object that tracks user inputs across multiple turns and triggers a mock API call only after collecting all required fields.

---

## WhatsApp Integration

To integrate with WhatsApp:

1. Use WhatsApp Business API (via Meta or Twilio)
2. Set up a webhook using Flask/FastAPI
3. Route incoming messages to this agent

Flow:
User → WhatsApp → Webhook → Agent → Response → WhatsApp
