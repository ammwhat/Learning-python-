import requests
import os
from bs4 import BeautifulSoup
import re
from email.message import EmailMessage
import smtplib

PRODUCT_URL = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
TARGET_PRICE = 52.00

SENDER_MAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
RECIEVER_MAIL = os.getenv("MY_EMAIL")

HEADERS = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36",
        "Accept-language" : "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
}

def fetch_product_price(url : str) -> tuple[str, float] :
    response = requests.get(url , headers=HEADERS)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "html.parser")
    product_container = soup.find("div", class_ = "col-sm-6 product_main")
    product_name = product_container.find("h1").get_text()
    price_element = soup.find('p', class_ = "price_color")
    raw_price = price_element.get_text()
    if not price_element:
        raise ValueError("Could not locate price element on page")
    title = product_name.strip()
    clener_price_str = re.sub(r"[^\d.]", "", raw_price.replace(",", ""))
    price = float(clener_price_str)

    return(title,price)

def send_price_alert(product_title :str, current_price :float, url:str) -> None:
    
    msg = EmailMessage()
    msg["Subject"] = f"Price Drop Alert : '{product_title[:30]}' "
    msg["From"] = SENDER_MAIL
    msg["To"] = RECIEVER_MAIL
    
    body = (
        f"Good news! \n\n"
        f"The price for {product_title} has dropped to {current_price:.2f} "
        f"The target price was {TARGET_PRICE} EURO "
        f"Buy it now : {url}"
     )
    msg.set_content(body)
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_MAIL, MY_PASSWORD)
        server.send_message(msg)
    print("email sent succesfully")
        
def main():
    try:
        title , current_price = fetch_product_price(PRODUCT_URL)  
        if current_price <= TARGET_PRICE:
            send_price_alert(title, current_price, PRODUCT_URL)
        else:
            print("price above threshold, no alert sent")
    except Exception as e:
        print(f"an error occured during price tracking : {e}")        

if __name__ == "__main__":
    main()           
        