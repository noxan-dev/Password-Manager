from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
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
    if len(website_input.get()) == 0 or len(email_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showinfo(title='Oops', message='Please input to all the fields.')
    else:
        is_ok = messagebox.askokcancel(title=website_input.get(), message=f'These are the details entered:\n'
                                                                          f'Email: {email_input.get()}\n'
                                                                          f'Password: {password_input.get()}.\n'
                                                                          f'Is this ok to save?')
        if is_ok:
            with open('data.txt', 'a') as data:
                data.write(
                    f'Website: {website_input.get()} | Email: {email_input.get()} | Password: {password_input.get()}\n')
                website_input.delete(0, END)
                password_input.delete(0, END)


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
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky='EW')
website_input.focus()

# Email Label
email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

# Email Input
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky='EW')

# Password Label
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Password Input
password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky='EW')

generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky='EW')

window.mainloop()
