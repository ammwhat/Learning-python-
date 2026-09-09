import requests
import os 
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
Appid = os.getenv("API_KEY")
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
my_number = os.getenv("PHONE_NUMBER")

OPEN_WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

parameter = {
    "appid" : Appid,
    "lat" : 23.23,
    "lon" : 76.87,
        
}
response = requests.get(url= OPEN_WEATHER_ENDPOINT, params=parameter)
response.raise_for_status()
data = response.json()
weather_data = data["list"]
twelve_hour_data = weather_data[:4]

will_rain = False
for item in twelve_hour_data:
    code = item["weather"][0]["id"]
    if code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token )
    message = client.messages.create(
        body = "Bring an umbrella",
        from_=  twilio_number,
        to = my_number
    )
    print(f"message sent SID : {message.sid}")
         
    
    
    