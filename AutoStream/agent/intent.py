# from google import genai

# client = genai.Client(api_key="YOUR_API_KEY")

# model = client.models.generate_content(
#     "gemini-2.5-flash-lite",
#     system_instruction="""
# Classify user intent into one of:
# - Greeting (when the user is just saying hi or starting a conversation)
# - Product Enquiry (when the user is asking about features, pricing, plans etc.)
# - High Intent (when the user is expressing strong interest or making a purchase intent)

# Only return the label.
# """
# )

# def detect_intent(user_input):
#     response = model.generate_content(user_input)
#     return response.text.strip()

# client = genai.Client(api_key="YOUR-API-KEY")

# def generate_greeting(user_input):
#     prompt = f"""
# You are a friendly AI assistant for a SaaS product called AutoStream.

# Respond naturally to the user's greeting and offer help.
# Keep it short and conversational.

# User: {user_input}
# Response:
# """

#     response = client.models.generate_content(
#         model="gemini-2.5-flash-lite",
#         contents=prompt
#     )

#     return response.text.strip()

import google.generativeai as genai

genai.configure(api_key="YOUR-API-KEY")

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction="""
Classify user intent into one of:
 - Greeting (when the user is just saying hi or starting a conversation)
 - Product Enquiry (when the user is asking about features, pricing, plans etc.)
 - High Intent (when the user is expressing strong interest or making a purchase intent)

Only return the label.
"""
)

def detect_intent(user_input):
    response = model.generate_content(user_input)
    return response.text.strip()

