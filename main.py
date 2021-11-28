from tkinter import *
from tkinter import messagebox
from tkinter import ttk
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
            'website': website
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
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
    # update the combobox
    update()


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
            messagebox.showinfo(title='No Website', message=f'No details for {user_entry} exists. '
                                                            f'Please add a website.')


# ---------------------------- UI SETUP/New Tab ------------------------------- #
window = Tk()
window.title('Password Generator')


notebook = ttk.Notebook(window, padding=10)
notebook.grid(column=0, row=0)

# create frames
new_tab = ttk.Frame(notebook, width=450, height=330)
existing_tab = ttk.Frame(notebook, width=450, height=330)

new_tab.grid(column=0, row=0)
existing_tab.grid(column=0, row=0)

# add frames to notebook
notebook.add(new_tab, text='New')
notebook.add(existing_tab, text='Existing')


# Style/theme
# style = Style()
# style.tk.call('source', 'sun-valley.tcl')
# style.tk.call('set_theme', 'dark')


# Image
canvas = Canvas(new_tab, width=200, height=200)
image = PhotoImage(file='logo.png')
canvas_image = canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)


# Website Label
website_label = Label(new_tab, text='Website:')
website_label.grid(column=0, row=1)

# Website Input
website_input = Entry(new_tab, width=21)
website_input.grid(column=1, row=1, sticky='EW')
website_input.focus()

# Email Label
email_label = Label(new_tab, text='Email/Username:')
email_label.grid(column=0, row=2)

# Email Input
email_input = Entry(new_tab, width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky='EW')

# Password Label
password_label = Label(new_tab, text='Password:')
password_label.grid(column=0, row=3)

# Password Input
password_input = Entry(new_tab, width=21)
password_input.grid(column=1, row=3, sticky='EW')

generate_button = Button(new_tab, text='Generate Password', width=15, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(new_tab, text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky='EW')

search_button = Button(new_tab, text='Search', width=15, command=find_password)
search_button.grid(column=2, row=1)


# ---------------------------- UI SETUP/Existing Tab ------------------------------- #
# Website listing

def combobox_used(event):
    website_input.delete(0, END)
    password_input.delete(0, END)
    email_input.delete(0, END)
    with open('data.json', 'r') as data_file:
        read_data = json.load(data_file)
        email = read_data[combobox.get()]["email"]
        password = read_data[combobox.get()]["password"]
        website = read_data[combobox.get()]["website"]

        # website_input.insert(0, website)
        # password_input.insert(0, password)
        # email_input.insert(0, email)
        show_website.config(text=website)
        show_email.config(text=email)
        show_password.config(text=password)


select_label = Label(existing_tab, text='Select an entry to view, edit, or delete')
select_label.grid(column=0, row=0, columnspan=4)


def update():
    with open('data.json', 'r') as data_file:
        read_data = json.load(data_file)
    website_list = [website for website in read_data]
    combobox['values'] = website_list


with open('data.json', 'r') as data:
    read_data = json.load(data)
    combobox = ttk.Combobox(existing_tab, text='Choose the website', width=30, justify='center')
    website_list = [website for website in read_data]
    combobox['values'] = website_list
    combobox.bind('<<ComboboxSelected>>', combobox_used)
    combobox.grid(column=0, row=1, columnspan=4, pady=10)


existing_website_label = Label(existing_tab, text='Website:')
existing_website_label.grid(column=0, row=2, pady=2, padx=15)
show_website = Label(existing_tab, text='Website')
show_website.grid(column=1, row=2, pady=2)
open_button = Button(existing_tab, text='Open')
open_button.grid(column=2, row=2, pady=2, padx=25)

existing_email_label = Label(existing_tab, text='Email/Username:')
existing_email_label.grid(column=0, row=3, pady=2, padx=15)
show_email = Label(existing_tab, text='Email')
show_email.grid(column=1, row=3, pady=2)
email_copy = Button(existing_tab, text='Copy')
email_copy.grid(column=2, row=3, pady=2, padx=25)

existing_password_label = Label(existing_tab, text='Password:')
existing_password_label.grid(column=0, row=4, pady=2, padx=15)
show_password = Label(existing_tab, text='Password')
show_password.grid(column=1, row=4, pady=2)
password_copy = Button(existing_tab, text='Copy')
password_copy.grid(column=2, row=4, pady=2, padx=25)

window.mainloop()
