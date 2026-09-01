import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("pomodoro timer")
label = tk.Label(window, text="", width = 20, height = 2, font = ("Arial", 16))
label.pack()
canvas = tk.Canvas(window, height=600, width=600)
canvas.pack()

image = Image.open("han_sohee.jpg")
image = ImageTk.PhotoImage(image)
canvas.create_image(300, 300, image=image)
timer_text = canvas.create_text(300,300, text= "25:00", font = ("Arial", 30, "bold"), fill = "white")

count = 0
timer_id = None
def count_down(count):
    minute = count//60
    second = count%60
    canvas.itemconfig(timer_text, text = f"{minute:02d}:{second:02d}")
    if count>0:
        global timer_id
        timer_id = window.after(1000, count_down, count-1)
    elif count == 0:
        start_timer() 
    

reps = 0

def start_timer():
    global reps
    stop_timer()
    reps+=1
 
    if reps % 2 == 0:
        count = 300
        label.config(text = "Break", fg = "green", font = ("Times New Roman", 40, "bold"))
    elif reps % 2 != 0:
        count = 1500
        label.config(text = "Work" , fg ="red", font = ("Georgia", 40, "bold"))
    count_down(count)      

def stop_timer():
    global timer_id
    if timer_id is not None:
        window.after_cancel(timer_id)
        timer_id = None       

def reset():
    global reps
    reps = 0
    window.after_cancel(timer_id)
    canvas.itemconfig(timer_text, text = "25:00")
    stop_timer()
    

Start_button = tk.Button(text="Start", command=start_timer)
Start_button.pack()
Reset_button = tk.Button(text = "Reset", command= reset)
Reset_button.pack()
window.mainloop()


