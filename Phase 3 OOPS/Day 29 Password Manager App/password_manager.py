import tkinter as tk
import random
import string

window = tk.Tk()
window.title("Password Manager")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50)

canvas = tk.Canvas(height=200, width=200)
raw_logo = tk.PhotoImage(file="logo.png")
logo_image = raw_logo.subsample(3,3)
canvas.create_image(100,100, image = logo_image)
canvas.grid(row=0, column=1)

website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = tk.Entry(width=35)
website_entry.grid(row=1,column=1, columnspan=2, sticky="w")

username_label = tk.Label(text = "Email/username:")
username_label.grid(row = 2, column=0)
username_entry = tk.Entry(width = 35)
username_entry.grid(row = 2, column=1, columnspan=2, sticky="w")

password_label = tk.Label(text = "password:")
password_label.grid(row = 3, column=0)
password_entry = tk.Entry(width = 35)
password_entry.grid(row=3,column=1, )

def generator(length = 16):
   characters = string.ascii_letters + string.digits + string.punctuation
   new_password = ''.join(random.choices(characters, k = length))  
   password_entry.delete(0, tk.END)
   password_entry.insert(0 , new_password)
 
generate_button = tk.Button(text="Generate Password", command= generator)
generate_button.grid(row=3, column=2)

def save():
   website = website_entry.get()
   username = username_entry.get()
   password = password_entry.get()
   with open("user_data.txt" , "a") as f:
      f.write(website + "\n")
      f.write(username + "\n")
      f.write(password + "\n")
   website_entry.delete(0, tk.END)
   username_entry.delete(0, tk.END)
   password_entry.delete(0, tk.END)   

add_button = tk.Button(text = "Add", command= save)
add_button.grid(column=0, row = 4,columnspan=3)

window.mainloop()

    



