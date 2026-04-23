from agent.state import state
from agent.tools import mock_lead_capture

def handle_lead_flow(user_input):
    if not state["name"]:
        state["name"] = user_input
        return "Great! What's your email?"

    elif not state["email"]:
        state["email"] = user_input
        return "Which platform do you create content on? (YouTube, Instagram, etc.)"

    elif not state["platform"]:
        state["platform"] = user_input

        mock_lead_capture(
            state["name"],
            state["email"],
            state["platform"]
        )

        state["collecting"] = False
        return "🎉 You're all set! Our team will contact you soon."

    return "Something went wrong."
