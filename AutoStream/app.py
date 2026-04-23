from agent.state import state
from agent.intent import detect_intent
from agent.rag import get_rag_answer
from agent.lead import handle_lead_flow

print("🚀 AutoStream AI Agent Started! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # 🔁 If already collecting lead info
    if state["collecting"]:
        reply = handle_lead_flow(user_input)
        print(f"Bot: {reply}")
        continue

    # 🧠 Detect intent
    intent = detect_intent(user_input)
    state["intent"] = intent

    print(f"(Detected Intent: {intent})")

    # 🎯 Routing
    if intent == "Greeting":
        print("Bot: Hello! How can I help you with AutoStream today?")

    elif intent == "Product Enquiry":
        answer = get_rag_answer(user_input)
        print(f"Bot: {answer}")

    elif intent == "High Intent":
        state["collecting"] = True
        print("Bot: Awesome! Let's get you started. What's your name?")

    else:
        print("Bot: I'm not sure I understood that. Could you rephrase?")
