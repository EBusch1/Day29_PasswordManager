import string
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# Day 29 - password manager
# - Password Generator - #
def generate_password():
    password_entry.delete(0, END)

    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    pwd_letters = [choice(letters) for _ in range(randint(8, 10))]
    pwd_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    pwd_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    pwd_list = pwd_letters + pwd_symbols + pwd_numbers
    shuffle(pwd_list)

    generated_password = "".join(pwd_list)

    password_entry.insert(END, generated_password)


# - Save Password - #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Checks if any fields are empty and provides specific field error.
    if len(email) == 0:
        messagebox.showerror(title="Empty email/username", message="Please enter a valid email/username")
    elif len(website) == 0:
        messagebox.showerror(title="Empty URL/Name", message="Please enter a valid URL/Name")
    elif len(password) == 0:
        messagebox.showerror(title="Empty password", message="Please enter a valid password")
    else:
        confirmed = messagebox.askokcancel(title=f"Confirmation for: {website}",
                                           message=f"Confirm credentials and click "
                                                   f"'Okay':\nUsername: {email}"
                                                   f"\nPassword: {password}")
        if confirmed:
            with open("vault.txt", "a") as vault_file:
                vault_file.write(f"{website} | {email} | {password}\n")
                # Copying saved password to clipboard
                pyperclip.copy(password)
                website_entry.delete(0, END)
                # email_entry.delete(0, END)
                password_entry.delete(0, END)


# - UI Setup - #

# Initialize default email
with open("email.txt", "r") as email_file:
    user_email = email_file.read()

# Create window
window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png, )
canvas.grid(row=0, column=1)
# canvas.pack()

# Labels
website_label = Label(text="Website URL/Name:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, user_email)
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

# Buttons
generate_pwd_button = Button(text="Generate Password", command=generate_password)
generate_pwd_button.grid(row=3, column=2)
add_button = Button(text="Store Password", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
