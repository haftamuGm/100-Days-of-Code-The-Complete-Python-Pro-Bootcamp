from tkinter import *
from tkinter import messagebox
from generator import password as x
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    pyperclip.copy(x)
    password_entry.insert(0,x)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data= {
        website_name: {
            "email":email,
            "password":password,
        }
    }
    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="unfill", message="Please Don't leave any field empty")
    else:
        try:
            with open("data.json","r") as data_file:
                data=json.load(data_file)
        except:
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file)
        else:
            data.update(new_data)
            with open("data.json","w") as f:
                json.dump(data,f,indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
def find_password():
    website_name = website_entry.get()
    password = password_entry.get()
    try:
        with open("data.json",'r') as f:
            data=json.load(f)
    except:
        messagebox.showinfo(title="Error",message="No data FileFound")
    else:
        if website_name in data:
            data[website_name]["email"]
            messagebox.showinfo(title=website_name,message=f"Email :{data[website_name]["email"]}\npassword:{data[website_name]["password"]}")
        else:
            messagebox.showinfo(title="Error",message=f"No Detail For {website_name} Exit")
    finally:
        website_entry.delete(0,END)

# Create the main window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Logo
image_lock = PhotoImage(file="logo.png")  # Ensure "logo.png" exists in the correct path
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image_lock)
canvas.grid(row=0, column=1)

# Labels
website = Label(text="Website:")
website.grid(row=1, column=0)
email = Label(text="Email/User:")
email.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)

# Entry fields
website_entry = Entry(width=24)
website_entry.focus()
website_entry.grid(row=1, column=1,columnspan=2)
email_entry = Entry(width=21)
email_entry.insert(0,"@gmail")
search=Button(text="Search",command=find_password)
search.grid(row=1,column=2)
email_entry.grid(row=2, column=1,columnspan=2)
password_entry = Entry(width=18)
password_entry.grid(row=3, column=1,columnspan=1)
# Buttons
generate = Button(text="Generate Password",command=generator)
generate.grid(row=3, column=2, pady=5)
add = Button(text="Add", width=36,command=save)
add.grid(row=4, column=1, columnspan=2)
# Run the application
window.mainloop()
