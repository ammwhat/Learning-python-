import requests
from bs4 import BeautifulSoup
import os 
from dotenv import load_dotenv
load_dotenv()
import smtplib
import time

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")


my_headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36",
    "Accept-language" : "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}
def product_details():
    product_link = str(input("Paste the url of your desried product : "))
    budget = float(input("Enter your desired price for the product: "))
    return product_link, budget

user_product_link, user_budget = product_details()

def check_price():
    response = requests.get(url= user_product_link, headers= my_headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    
    price_tag = soup.find("span", class_="a-price-whole") or soup.find(class_="price")
    if not price_tag:
        print("Price element not found, check ur CSS selectors")
        return 
    raw_price = price_tag.get_text()
    cleaned_price = float(raw_price.replace("₹", "").replace("$", "").replace(",", "").strip())
    if cleaned_price <= user_budget:
        send_alert(user_product_link, cleaned_price)
    
def send_alert(url, price):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user= MY_EMAIL, password= MY_PASSWORD)
            connection.sendmail(
                from_addr = MY_EMAIL,
                to_addrs= MY_EMAIL,
                msg= f"Subject : PRICE DROP ALERT\n\n Your product {url}, is within ur budget with {price} "
            )
            print("Email successfully dispatched!")    

if __name__ == "__main__" :
    while True:
        check_price()
        time.sleep(21600)
                
        
            
    
