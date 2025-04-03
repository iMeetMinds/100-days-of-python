from tkinter import *
from tkinter import messagebox
import random
import pyperclip

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

    if len(web_in) == 0 or len(email_in) == 0 or len(pass_in) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any field empty!!")
    else:
        is_okay = messagebox.askokcancel(title=web_in, message=f"There are the details entered: \nEmail: {email_in} "
                                                     f"\nPassword: {pass_in} \nIs it okay to save?")
        if is_okay:
            with open("data.txt", mode='a') as pass_file:
                text = f"{web_in} || {email_in} || {pass_in} \n"
                pass_file.write(text)
                website_input.delete(0, END)
                password_input.delete(0, END)

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


website_input = Entry(width=40)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
email_input = Entry(width=40)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "example@gmail.com")
password_input = Entry(width=20)
password_input.grid(column=1, row=3)


gen_password_btn = Button(text="Generate Password", command=password_generator)
gen_password_btn.grid(column=2, row=3)
add_button = Button(text="Add", width=35, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()