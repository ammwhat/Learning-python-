import csv
import datetime
from pathlib import Path
import os 
import random

today = datetime.date.today()
current_month = today.month
current_day = today.day

base_folder = Path(__file__).resolve().parent
birthdays_file = base_folder / "birthdays.csv"
template_folder_path = base_folder / "birthday templates"
templates = os.listdir(template_folder_path)

with open(birthdays_file, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        name = row[0]
        email = row[1]
        birth_month = int(row[3])
        birth_day = int(row[4])

        if birth_month == current_month and birth_day == current_day:
            print(f"Match found: ready to send email to {name} at {email}")
            random_template = random.choice(templates)
            template_path = template_folder_path / random_template
            with open(template_path, 'r') as f:
                letter = f.read()
            new_letter = letter.replace("[NAME]", name)    

                
            
            
            




            
