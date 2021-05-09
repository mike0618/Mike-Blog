from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
LIGHTRED = "#de6463"
RED = "#c30202"
GREEN = "#2f4320"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
text = '✔'
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps, timer
    if timer:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    label.config(text='Timer', fg=GREEN)
    check_label.config(text='')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    if reps == 0:
        start_timer()


def start_timer():
    global reps
    reps += 1
    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if not reps % 8:
        countdown(long_break)
        label.config(text='Long Break', fg=LIGHTRED)
    elif reps % 2:
        countdown(work)
        label.config(text='Work', fg=GREEN)
    else:
        countdown(short_break)
        label.config(text='Break', fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minutes, seconds = divmod(count, 60)
    canvas.itemconfig(timer_text, text=f"{f'0{minutes}'[-2:]}:{f'0{seconds}'[-2:]}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        check_label.config(text=text * (reps // 2))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.minsize(width=550, height=500)
window.config(padx=50, pady=30, bg=YELLOW)

canvas = Canvas(width=300, height=308, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(150, 154, image=tomato)
timer_text = canvas.create_text(150, 180, text='00:00', fill=YELLOW, font=(FONT_NAME, 55, 'bold'))
canvas.grid(row=1, column=1)
window.iconphoto(False, tomato)

label = Label(padx=5, pady=5, text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 34, 'bold'))
label.grid(row=0, column=1)
check_label = Label(padx=5, pady=5, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 34, 'bold'))
check_label.grid(row=3, column=1)

startbtn = Button(text='Start', fg=GREEN, bg=YELLOW, activeforeground=GREEN, activebackground=YELLOW,
                  highlightthickness=0, font=(FONT_NAME, 13, 'bold'), command=start)
startbtn.grid(row=2, column=0)
resetbtn = Button(text='Reset', fg=GREEN, bg=YELLOW, activeforeground=GREEN, activebackground=YELLOW,
                  highlightthickness=0, font=(FONT_NAME, 13, 'bold'), command=reset)
resetbtn.grid(row=2, column=2)

window.mainloop()
