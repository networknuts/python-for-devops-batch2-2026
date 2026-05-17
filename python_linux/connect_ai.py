import requests
from dotenv import load_dotenv
import os 
import json 

# SYSTEM INSTRUCTIONS
SYSTEM_INSTRUCTIONS = """
You are a devops AI assistant, you are only supposed to
answer queries related to devops.
If the user ends up asking a non-devops question, then please
straightaway refuse the request of the user.
"""

# ASK USER FOR INPUT
USER_QUERY = input("Enter your query: ")

#READING KEY AND VALUE PAIRS FROM THE .env FILE
load_dotenv()

#FETCH THE API KEY FROM THE .env FILE
API_KEY = os.getenv("OPENAI_API_KEY")

# PROVIDE THE ENDPOINT URL FROM OPENAI DOCUMENTATION
AI_URL = "https://api.openai.com/v1/responses"

# DEFINE HEADERS AS PER OPENAI DOCUMENTATION
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# DEFINE DATA AS PER OPENAI DOCUMENTATION
PAYLOAD = {
    "model": "gpt-5.4-mini",
    "instructions": SYSTEM_INSTRUCTIONS,
    "input": USER_QUERY
}

response = requests.post(
    AI_URL,
    headers=HEADERS,
    data=json.dumps(PAYLOAD)
)

print("AI RESPONSE\n")
result = response.json()
print(result['output'][0]['content'][0]['text'])