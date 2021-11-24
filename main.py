from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# from tkinter.ttk import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    pass_list = pass_letters + pass_symbols + pass_numbers
    shuffle(pass_list)

    password = "".join(pass_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get().capitalize()
    password = password_input.get()
    email = email_input.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }
    if len(website) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='Please input to all the fields.')
    else:
        try:
            with open('data.json', 'r') as data:
                update_data = json.load(data)
        except (FileNotFoundError, ValueError):
            with open('data.json', 'w') as data:
                json.dump(new_data, data, indent=4)
        else:
            update_data.update(new_data)

            with open('data.json', 'w') as data:
                json.dump(update_data, data, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


def find_password():
    user_entry = website_input.get().capitalize()
    try:
        with open('data.json', 'r') as data:
            read_data = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title='No File', message='No Data File Found.')
    else:
        if len(user_entry) == 0:
            messagebox.showinfo(title='Oops', message='Please input to all the fields.')
        elif user_entry in read_data:
            email = read_data[user_entry]["email"]
            password = read_data[user_entry]["password"]
            messagebox.showinfo(title=user_entry, message=f'Email: {email}\nPassword: {password}')
        else:
            messagebox.showinfo(title='No Website', message=f'No details for {user_entry} exists. Please add a website.')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Generator')
window.config(padx=50, pady=50)

# Style/theme
# style = Style()
# style.tk.call('source', 'sun-valley.tcl')
# style.tk.call('set_theme', 'dark')


# Image
canvas = Canvas(width=200, height=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Website Label
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

# Website Input
website_input = Entry(width=21)
website_input.grid(column=1, row=1, sticky='EW')
website_input.focus()

# Email Label
email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

# Email Input
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky='EW')
email_input.insert(0, 'chaimmalek@gmail.com')

# Password Label
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Password Input
password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky='EW')

generate_button = Button(text='Generate Password', width=15, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky='EW')

search_button = Button(text='Search', width=15, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
