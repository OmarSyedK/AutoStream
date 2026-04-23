import json
import google.generativeai as genai

# configure Gemini
genai.configure(api_key="YOUR-API-KEY")
model = genai.GenerativeModel("gemini-2.5-flash")

# load knowledge
with open("data/knowledge.json") as f:
    knowledge = json.load(f)

def get_rag_answer(query):
    context = json.dumps(knowledge, indent=2)

    prompt = f"""
    You are an AutoStream assistant. Help the user with their queries and answer humanely.

    Answer ONLY using the knowledge below.
    Do NOT make up information.Ok 

    Knowledge:
    {context}

    Question: {query}
    """

    response = model.generate_content(prompt)
    return response.text
