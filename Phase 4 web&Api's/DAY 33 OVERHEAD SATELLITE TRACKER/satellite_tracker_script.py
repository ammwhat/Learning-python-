import requests
import time 
import datetime
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()  

MY_EMAIL = os.getenv("MY_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

my_latitude = 23.0175
my_longitude = 76.7221

iss_endpoint = "http://api.open-notify.org/iss-now.json"
sunset_sunrise_api = "https://api.sunrisesunset.io/json"

def is_overhead(iss_lat, iss_long):
  return (iss_lat - 5 <= my_latitude <= iss_lat + 5) and (iss_long -5 <= my_longitude <= iss_long + 5)

def is_night():
  params = {
        "lat" : my_latitude,
        "long" : my_longitude,
      }
  response = requests.get(url = sunset_sunrise_api, params= params)
  response.raise_for_status()
  sun_data = response.json()
  sunrise = sun_data["results"]["sunrise"]
  sunset = sun_data["results"]["sunset"]
  sunrise_hour = datetime.datetime.strptime(sunrise, "%I:%M:%S %p").hour
  sunset_hour = datetime.datetime.strptime(sunset, "%I:%M:%S %p").hour
  time_now = datetime.datetime.now().hour

  if time_now >= sunset_hour or time_now <= sunrise_hour:
    return True
  return False
  
while True:
  try:
    response = requests.get(url= iss_endpoint)
    response.raise_for_status()
    data = response.json()
    
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    
    print(f"Current ISS Position -> latitude : {latitude}, longitude : {longitude}")

    if is_overhead(latitude, longitude) and is_night():
       with smtplib.SMTP("smto.gmail.com", 587) as connection:
          connection.starttls()
          connection.login(user= MY_EMAIL, password= APP_PASSWORD)
          connection.sendmail(
            from_addr= MY_EMAIL,
            to_addrs= MY_EMAIL,
            msg = "Subject : ISS ALERT\n\nLook up! The ISS is above you!"
          )
  except Exception as e:
    print(f"Error fetching telemetry: {e}")    
  time.sleep(60) 

          
      
      

  


  
 

 