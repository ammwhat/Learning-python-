from bs4 import BeautifulSoup
from pathlib import Path
import os 
from dotenv import load_dotenv
load_dotenv()
import smtplib

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

BASE_DIR = Path(__file__).resolve().parent
flightdata_path = BASE_DIR/"Flight_data.html"

with flightdata_path.open('r', encoding="utf-8") as f:
    html_content = f.read()
soup = BeautifulSoup(html_content, 'html.parser')


def get_details():
    destination = input("WHERE U WANNA GO TO (ZRH/FCO/CPH): ").upper()  
    budget = float(input("WHAT'S UR MAXIMUM BUDGET BROKE BOY: "))
    return destination, budget
my_dest , my_budget = get_details()

flight_cards = soup.find_all("div", class_  = "flight-card")
for card in flight_cards:
    destination = card.find("span", class_ = "destination").get_text()
    raw_price = card.find("span", class_ = "price").get_text()
    clean_price =float(raw_price.replace(",",""))    
    if my_dest == destination and my_budget >= clean_price:
     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user= MY_EMAIL, password= MY_PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs= MY_EMAIL,
            msg= f"Subject : pack ur bags\n\n your foriegn trip from DEL TO {my_dest} IS POSSIBLE "
        )
        print("Email successfully dispatched!")    


    
            
    

    
     
    