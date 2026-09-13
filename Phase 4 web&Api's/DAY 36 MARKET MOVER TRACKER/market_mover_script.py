import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

alpha_vantage_api = os.getenv("ALPHA_VANTAGE")
news_api = os.getenv("NEWS_API")
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
my_number = os.getenv("PHONE_NUMBER")


print("when entering NON US COMPANIES ADD .SUFFIX FOR EX: .BSE FOR INDIAN COMPANIES")
asset_name = input("enter the asset name for which you want alerts:").strip().upper()
asset_name_news = asset_name.split(".")[0]

alpha_vantage_endpoint = "https://www.alphavantage.co/query"
news_api_endpoint = "https://newsapi.org/v2/everything"

parameter = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : asset_name,
    "apikey" : alpha_vantage_api
    
}
paramter_2 = {
    "q" :  asset_name_news,
    "apiKey" : news_api,
    "language" : "en",
    "sortBy" : "relevancy",
    "pageSize" : 3

    }
repsonse = requests.get(url = alpha_vantage_endpoint, params = parameter)
repsonse.raise_for_status()
data = repsonse.json()["Time Series (Daily)"]
date_list = [date for date in data]
yesterday = date_list[0]
day_before_yesterday = date_list[1]

yesterday_closingprice = float(data[yesterday]["4. close"])
day_before_yesterday_closingprice = float(data[day_before_yesterday]["4. close"])
diff = (yesterday_closingprice - day_before_yesterday_closingprice) 
percentage_diff = (diff / day_before_yesterday_closingprice) * 100

if percentage_diff > 0.05 or percentage_diff < -0.05:
    news_response = requests.get(url=news_api_endpoint, params= paramter_2)
    news_response.raise_for_status()
    articels = news_response.json().get("articles", [])
    news_summary = ""
    for article in articels:
        title = article.get("title")
        news_summary += f"\n.{title}"
    message_body = f"Headlines News : {news_summary}"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = message_body,
        from_= "whatsapp:+17372212163",
        to = f"whatsapp:{my_number}"
                
    )
    print(f"SMS Alert sent! Message SID: {message.sid}")
    
        
        
        
        
    
    
    
    
    

