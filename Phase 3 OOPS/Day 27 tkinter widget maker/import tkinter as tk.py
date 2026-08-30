import tkinter as tk

window = tk.Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)
# the label widget
my_label = tk.Label(text = "Enter your name:", font = ("Arial", 14))
my_label.pack()
# the entry widget
input_box = tk.Entry(width = 30)
input_box.pack()
#button function 
def button_clicked():
    new_text = input_box.get()
    my_label.config(text= f"Hello, {new_text}")
#button widget
button = tk.Button(text="click me", command=button_clicked)
button.pack()
window.mainloop()    
