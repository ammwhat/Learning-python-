import requests
import os
from dotenv import load_dotenv
import datetime
import json 
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API")
SHEETY_TOKEN = (os.getenv("SHEETY_TOKEN") or "").strip()
gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key={GEMINI_API_KEY}"
sheety_endpoint = "https://api.sheety.co/b13c0daf57e8bcbde4414ae958f605e1/workout/sheet1"

if not SHEETY_TOKEN:
    raise RuntimeError("SHEETY_TOKEN is missing from .env")

user_input = input("what did you do for workout today:")

system_prompt = """
You are a workout parser API. 
Extract exercise data from the user input and output ONLY a valid JSON object.
Do not include any Markdown formatting, backticks, or extra text.

Required JSON Structure:
{
    "exercise": "string",
    "duration_min": integer,
    "calories_burned": integer
}
"""
combined_text = f"{system_prompt}\n\nUser Input : {user_input}"
payload = {
    "contents" : [{"parts": [{"text":combined_text}]}]
}
response = requests.post(url= gemini_url, json= payload )
response.raise_for_status()
data = response.json()
raw_text = data["candidates"][0]["content"]["parts"][0]["text"]
parsed_data = json.loads(raw_text)
today = datetime.datetime.now()
date_str = today.strftime("%d/%m/%y")
time_str = today.strftime("%X")
sheety_payload = {
    "sheet1" : {
        "date" : date_str,
        "time" : time_str,
        "exercise" : parsed_data["exercise"],
        "duration" : parsed_data["duration_min"],
        "calories" : parsed_data["calories_burned"]
    }
    
}
header = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}
sheety_reponse = requests.post(url=sheety_endpoint, json=sheety_payload, headers=header)
try:
    sheety_reponse.raise_for_status()
except requests.HTTPError as error:
    if sheety_reponse.status_code == 401:
        raise RuntimeError(
            "Sheety rejected SHEETY_TOKEN. Generate a new token for this project "
            "and replace the value in .env."
        ) from error
    if sheety_reponse.status_code == 400:
        raise RuntimeError(
            f"Sheety rejected the request body: {sheety_reponse.text}"
        ) from error
    raise
print(sheety_reponse.text)