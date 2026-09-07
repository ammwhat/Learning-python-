import tkinter as tk
import random 
import json
from pathlib import Path

window = tk.Tk()
window.title("flash card learning application")
window.minsize(width=600, height=600)
window.config(padx=100, pady=100)

flashcard = tk.Canvas(width=200, height=200)
flashcard.grid(row=0, column=0, rowspan=2)

BASE_DIR = Path(__file__).resolve().parent
JSON_FILE = BASE_DIR/ "words.json"

with JSON_FILE.open("r", encoding = "utf-8") as file:
    data = json.load(file)

current_card = {}
timer = None
card_word = flashcard.create_text(100,100 , text = "")

def next_card():
    global current_card, timer
    if timer is not None:
        window.after_cancel(timer)
        timer = None
    current_card = random.choice(data)
    flashcard.itemconfig(card_word, text = current_card["French"])
    timer = window.after(3000, flip)
      
def flip():
    if current_card:
        flashcard.itemconfig(card_word, text = current_card["English"])

def right():
    data.remove(current_card)
    with JSON_FILE.open('w', encoding= "utf-8") as file:
        json.dump(data, file)
    next_card()

def wrong():
    next_card()

right_button = tk.Button(text= "Right", command= right)
right_button.grid(row = 1, column=0)

wrong_button = tk.Button(text = "Wrong", command = wrong)
wrong_button.grid(row = 1, column=1)

next_card()
window.mainloop()

