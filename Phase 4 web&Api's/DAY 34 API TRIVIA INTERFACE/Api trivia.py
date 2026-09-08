import requests
import tkinter as tk
import html

Open_TDP_endpoint= "https://opentdb.com/api.php"
params = {
    "amount" : 10,
    "type" : "boolean" 
}
response = requests.get(url= Open_TDP_endpoint, params= params)
response.raise_for_status()
data = response.json()

question_bank = data["results"]
score = 0
current_question = {}

window = tk.Tk()
window.config(width=600, height=600)
window.title("Quiz")
window.config(padx=50,pady=50)

score_label = tk.Label(text= f"Score : {score}" , font = ("arial", 16))
score_label.grid(row = 0, column=1)
canvas = tk.Canvas(height=250 , width=400)
canvas.grid(row=1, column=0 , rowspan=2, pady=50)

display = canvas.create_text(200, 80 , text = "", width=380 , font = ("arial", 20 , "bold"))

def next_ques():
    global current_question
    if len(question_bank) > 0:
        true_button.config(bg = "blue")
        false_button.config(bg = "blue")
        true_button.config(state="normal")
        false_button.config(state="normal")
        current_question = question_bank.pop(0)
        question_text = html.unescape(current_question["question"])
        canvas.itemconfig(display, text = question_text)
    else:
        canvas.itemconfig(display, text = "you've reached end of quiz")
        true_button.config(state="disabled")
        false_button.config(state="disabled")

def check_answer(user_guess):
    global score
    correct_answer = current_question["correct_answer"]            
    if user_guess == correct_answer:
        score += 1
        score_label.config(text = f"Score : {score}")
        if user_guess == "True":
            true_button.config(bg = "green")
        else:
            false_button.config(bg = "green")    
    else: 
        if user_guess == "True":
            true_button.config(bg = "red")
        else :
            false_button.config(bg = "red")    

    window.after(1000, next_ques)      

def correct():
    check_answer("True")
def incorrect():
    check_answer("False")    
true_button = tk.Button(text= "True", bg="blue", fg= "white", command= correct)
true_button.grid(row = 2, column=0, sticky= "w")
false_button = tk.Button(text="False", bg = "blue", fg = "white" ,command= incorrect)
false_button.grid(row = 2 , column=1, sticky="w")     
        
next_ques()
window.mainloop()   
      
      
     
    



