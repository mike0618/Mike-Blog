from tkinter import *
from tkinter import messagebox, ttk
from string import ascii_lowercase, ascii_uppercase, digits
from random import randint, choice, shuffle
import pyperclip
import json


# ------------------------------- INITIALIZATION -------------------------------- #
def init_file():
    with open('data.json', 'w') as f:
        json.dump({'website': {'login': 'password'}}, f, indent=4)


try:
    json.load(open('data.json', 'r'))
except FileNotFoundError:
    init_file()
except json.JSONDecodeError:
    init_file()


# ---------------------------- ENCRYPTION/DECRYPTION ---------------------------- #
def crypt(pw, decrypt=False):
    key = key_entry.get()
    password = ''
    if key:
        if decrypt:
            pw = pw.split('/')[:-1]
            for i in range(len(pw)):
                password += chr(int(pw[i]) ^ ord(key[i % len(key)]))
        else:
            for i in range(len(pw)):
                password += f'{ord(pw[i]) ^ ord(key[i % len(key)])}/'
    return password


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def passgen():
    l_list = [choice(ascii_lowercase) for _ in range(randint(3, 5))]
    up_list = [choice(ascii_uppercase) for _ in range(randint(3, 5))]
    n_list = [choice(digits) for _ in range(randint(2, 4))]
    s_list = [choice('!?#$%&*()+-,.') for _ in range(randint(2, 4))]

    password_list = l_list + up_list + n_list + s_list
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(END, password)
    pyperclip.copy(password)
    info_label.config(fg='#499c59', text='New password copied to clipboard')


# ---------------------------- SHOW/HIDE PASSWORDS ------------------------------- #
def show():
    text.delete(1.0, END)
    site = site_combo.get()
    login = login_combo.get()
    if site and login:
        info_label.config(text='')
        with open('data.json', 'r') as f:
            data = json.load(f)
            if site in data and login in data[site]:
                pw = data[site][login]
                insert = '*' * 50 + f'\nWebsite: {site}\nLogin: {login}\nPassword: '
                if key_entry.get():
                    text.insert(END, insert + f'{crypt(pw, True)}\n' + '*' * 50)
                else:
                    text.insert(END, insert + 'Please enter a SECRET WORD\n' + '*' * 50)
                text.grid(row=6, column=0, columnspan=3)
                text.focus()
            else:
                info_label.config(fg='#fec269', text='Nothing to show')
                text.grid_remove()
    else:
        info_label.config(fg='#fec269', text='Fill out the "Website" and "Login" fields')
        text.grid_remove()


def hide():
    key_entry.delete(0, END)
    pass_entry.delete(0, END)
    login_combo.delete(0, END)
    text.grid_remove()
    text.delete(1.0, END)
    info_label.config(fg='#fec269', text="SECRET WORD CLEARED")


# ---------------------------- SAVE PASSWORD -------------------------------- #
def save():
    text.grid_remove()
    text.delete(1.0, END)
    site = site_combo.get()
    login = login_combo.get()
    passw = pass_entry.get()

    if site and login and passw and key_entry.get():
        new_data = {site: {login: crypt(passw)}}
        with open('data.json', 'r') as f:
            data = json.load(f)
            if site in data:
                if login in data[site]:
                    if not messagebox.askyesno('Login exists', 'Do replace the password?'):
                        return 'login exists'
                data[site].update(new_data[site])
            else:
                data.update(new_data)
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)

            login_combo.delete(0, END)
            pass_entry.delete(0, END)
            info_label.config(fg='#499c59', text=f'Entry for {site} added')
            site_combo.delete(0, END)
    else:
        info_label.config(fg='#fec269', text='Fill out the form')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
icon = PhotoImage(file='icon.png')
window.title('Password Manager')
window.minsize(width=600, height=310)
window.config(padx=30, pady=20, bg='#363636')
window.iconphoto(False, icon)

canvas = Canvas(width=320, height=140, bg='#363636', highlightthickness=0)
logo = PhotoImage(file='key.png')
canvas.create_image(160, 70, image=logo)
logo_text = canvas.create_text(200, 45, text='My Pass', fill='#fec269', font=('Courier', 21, 'bold italic'))
canvas.grid(row=0, column=0, columnspan=2, rowspan=2)

site_label = Label(pady=5, text='Website:', fg='white', bg='#363636', font=('Courier', 13, 'bold'))
site_label.grid(row=2, column=0, sticky='e')
login_label = Label(pady=5, text='Login:', fg='white', bg='#363636', font=('Courier', 13, 'bold'))
login_label.grid(row=3, column=0, sticky='e')
pass_label = Label(pady=5, text='Password:', fg='white', bg='#363636', font=('Courier', 13, 'bold'))
pass_label.grid(row=4, column=0, sticky='e')
info_label = Label(pady=5, text='', fg='#499c59', bg='#363636', font=('Courier', 13, 'bold'))
info_label.grid(row=7, column=1, columnspan=2)
key_label = Label(text='SECRET WORD:', fg='white', bg='#363636', font=('Courier', 13, 'bold'))
key_label.grid(row=0, column=2, sticky='s')


def sitelist():
    with open('data.json') as f:
        data = json.load(f)
        site_combo['values'] = sorted([site for site in data.keys()])


def loginlist():
    login_combo['values'] = []
    if site_combo.get():
        with open('data.json') as f:
            data = json.load(f)
            if site_combo.get() in data:
                data = data[site_combo.get()]
                login_combo['values'] = sorted([login for login in data.keys()])


site_combo = ttk.Combobox(width=54, postcommand=sitelist)
site_combo.focus()
site_combo.grid(pady=3, row=2, column=1, columnspan=2, sticky='w')
login_combo = ttk.Combobox(width=54, postcommand=loginlist)
login_combo.grid(row=3, column=1, columnspan=2, sticky='w')

pass_entry = Entry(width=34)
pass_entry.grid(row=4, column=1, sticky='w')
key_entry = Entry(width=20, fg='white', bg='white')
key_entry.grid(row=1, column=2, sticky='n')

gen_btn = Button(padx=43, pady=1, text="Generate", anchor='s', highlightthickness=0, fg='white', bg='#363636',
                 activeforeground='white', activebackground='#595959', font=('Courier', 13, 'normal'), command=passgen)
gen_btn.grid(row=4, column=2)
show_btn = Button(padx=118, pady=1, text="Show", anchor='s', highlightthickness=0, fg='white', bg='#363636',
                  activeforeground='white', activebackground='#7d5d30', font=('Courier', 13, 'normal'), command=show)
show_btn.grid(row=5, column=1, sticky='w')
hide_btn = Button(padx=24, pady=1, text="Hide", anchor='s', highlightthickness=0, fg='white', bg='#7d5d30',
                  activeforeground='white', activebackground='#499c59', font=('Courier', 13, 'normal'), command=hide)
hide_btn.grid(row=5, column=0)
add_btn = Button(padx=68, pady=1, text="Add", anchor='s', highlightthickness=0, fg='white', bg='#363636',
                 activeforeground='white', activebackground='#499c59', font=('Courier', 13, 'normal'), command=save)
add_btn.grid(pady=3, row=5, column=2)

text = Text(width=67, height=5)

window.mainloop()
