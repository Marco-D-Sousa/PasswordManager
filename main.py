from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    entry_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['@', '!', '%', '+']

    password_letters = [choice(letters) for _ in range(randint(4, 6))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = ''.join(password_list)
    entry_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    password = entry_password.get()
    website = entry_website.get()
    email = entry_email.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Email: {email}\n Password: {password}\n Is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

# Entries
entry_website = Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()

entry_email = Entry(width=35)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(index=0, string='marco@email.com')

entry_password = Entry(width=21)
entry_password.grid(column=1, row=3)

# Buttons
btn_generate_password = Button(text="Generate", command=generate_password)
btn_generate_password.grid(column=2, row=3)

btn_add = Button(text="Add", width=36, command=save)
btn_add.grid(column=1, row=4)

window.mainloop()
