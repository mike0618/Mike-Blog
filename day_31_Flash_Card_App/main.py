from tkinter import *
import pandas as pd
from random import choice

# ==================== INITIALIZATION ========================= #
try:
    df = pd.read_csv('./data/words_to_learn.csv')
except (FileNotFoundError, pd.errors.EmptyDataError):
    df = pd.read_csv('./data/french_words.csv')
else:
    if not df.to_dict(orient='records'):
        df = pd.read_csv('./data/french_words.csv')

cards = df.to_dict(orient='records')
card = {}


# ====================== FUNCTIONS ============================ #
def i_khow():
    if cards:
        cards.remove(card)
        df = pd.DataFrame(cards)
        df.to_csv('./data/words_to_learn.csv', index=False)
        next_card()


def next_card():
    global flip_timer
    global card
    if cards:
        card = choice(cards)
        window.after_cancel(flip_timer)
        canvas.itemconfig(canvas_image, image=image_front)
        canvas.itemconfig(card_title, text='French', fill='black')
        canvas.itemconfig(card_word, text=card['French'], fill='black')

        def flip_card():
            canvas.itemconfig(canvas_image, image=image_back)
            canvas.itemconfig(card_title, text='English', fill='white')
            canvas.itemconfig(card_word, text=card['English'], fill='white')

        flip_timer = window.after(3000, flip_card)
    else:
        window.after_cancel(flip_timer)
        canvas.itemconfig(card_title, text='Congratulations!', fill='#ed3359')
        canvas.itemconfig(card_word, text="You've got it!", fill='#ed3359')


# ====================== UI SETUP ============================== #
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
image_front = PhotoImage(file='./images/card_front.png')
image_back = PhotoImage(file='./images/card_back.png')
image_wrong = PhotoImage(file='./images/wrong.png')
image_right = PhotoImage(file='./images/right.png')
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.iconphoto(False, image_right)

flip_timer = window.after(500, next_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=image_front)
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

button_wrong = Button(image=image_wrong, activebackground=BACKGROUND_COLOR, bg=BACKGROUND_COLOR, highlightthickness=0,
                      bd=0, command=next_card)
button_right = Button(image=image_right, activebackground=BACKGROUND_COLOR, bg=BACKGROUND_COLOR, highlightthickness=0,
                      bd=0, command=i_khow)
button_wrong.grid(row=1, column=0)
button_right.grid(row=1, column=1)

window.mainloop()
