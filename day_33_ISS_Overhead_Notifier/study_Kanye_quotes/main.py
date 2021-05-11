from tkinter import *
import requests


def get_quote():
    response = requests.get(url='https://api.kanye.rest/')
    response.raise_for_status()
    canvas.itemconfig(quote_text, text=response.json()['quote'])


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg='#09d9d9')

canvas = Canvas(width=300, height=414, bg='#09d9d9', highlightthickness=0)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 21, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(bd=0, image=kanye_img, highlightthickness=0, command=get_quote, activebackground='#09d9d9',
                      bg='#09d9d9')
kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()
