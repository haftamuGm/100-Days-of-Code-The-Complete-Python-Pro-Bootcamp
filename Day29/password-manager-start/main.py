from tkinter import *
from tkinter import messagebox
from generator import password as x
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    pyperclip.copy(x)
    password_entry.insert(0,x)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="unfill", message="Please Don't leave any field empty")
    else:
        is_ok=messagebox.askokcancel(title="mx",message="Type 'Ok' To Enter All Data")
        if is_ok:
            with open("data.txt",mode='a') as file:
                file.write(f"{website_name}|{email}|{password}\n")
                website_entry.delete(0,END)
                email_entry.delete(0,END)
                password_entry.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #


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
website.grid(row=1, column=0, pady=5)
email = Label(text="Email/User:")
email.grid(row=2, column=0, pady=5)
password = Label(text="Password:")
password.grid(row=3, column=0, pady=5)

# Entry fields
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, pady=5)
email_entry = Entry(width=35)
email_entry.insert(0,"@gmail")
email_entry.grid(row=2, column=1, columnspan=2, pady=5)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, pady=5)
# Buttons
generate = Button(text="Generate Password",command=generator)
generate.grid(row=3, column=2, pady=5)
add = Button(text="Add", width=36,command=save)
add.grid(row=4, column=1, columnspan=2)
# Run the application
window.mainloop()
