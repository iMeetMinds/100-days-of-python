from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_input.delete(0, END)
    final_pass_list = []
    nr_letters = [random.choice(LETTERS) for n in range(random.randint(8,10))]
    nr_symbols = [random.choice(NUMBERS) for n in range(random.randint(2,4))]
    nr_numbers = [random.choice(SYMBOLS) for n in range(random.randint(2,4))]
    final_pass_list = nr_letters + nr_symbols + nr_numbers
    random.shuffle(final_pass_list)
    password = "".join(final_pass_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web_in = website_input.get()
    email_in = email_input.get()
    pass_in = password_input.get()

    json_data = {
        web_in : {
            "email" : email_in,
            "password" : pass_in
        }
    }

    if len(web_in) == 0 or len(email_in) == 0 or len(pass_in) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any field empty!!")
    else:
        try:
            with open("data.json", mode='r') as pass_file:
                # Read olf file
                file_data = json.load(pass_file)
        except FileNotFoundError:
            with open("data.json", mode='w') as manage_file:
                # Saving updated data
                json.dump(json_data, manage_file, indent=4)
        else:
            # Updating new data
            file_data.update(json_data)
            pass_file.close()
            with open("data.json", mode='w') as manage_file:
                # Saving updated data
                json.dump(file_data, manage_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

def find_password():
    web_in = website_input.get()

    if not len(web_in) > 0 :
        messagebox.showerror(title="Oops", message="Please don't leave website field empty!!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                json_file = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror(title="Oops", message="No Data file found!!")
        else:
            if web_in in  json_file:
                email_need = json_file[web_in]["email"]
                pass_need = json_file[web_in]["password"]
                messagebox.showinfo(title=web_in, message=f"Email: {email_need} \nPassword: {pass_need}")
            else:
                messagebox.showerror(title="Oops", message="No Details for the website exits!!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)


website_input = Entry(width=20, justify='left')
website_input.grid(column=1, row=1)
website_input.focus()
email_input = Entry(width=50, justify='left')
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "example@gmail.com")
password_input = Entry(width=20, justify='left')
password_input.grid(column=1, row=3)


search_btn = Button(text="Search", command=find_password, width=20, justify='left')
search_btn.grid(column=2, row=1)
gen_password_btn = Button(text="Generate Password", command=password_generator, width=20, justify='left')
gen_password_btn.grid(column=2, row=3)
add_button = Button(text="Add", width=35, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()