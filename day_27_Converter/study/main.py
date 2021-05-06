import tkinter

window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=200, pady=200)

# Label
my_label = tkinter.Label(text='Text here', font=('Arial', 24, 'bold'))
my_label.grid(row=0, column=0)
new_label = tkinter.Label()
new_label.grid(row=1, column=0)
# new_label.config(text="New text")
# other_label = tkinter.Label()
# other_label.pack(side='bottom')
# other_label['text'] = 'Text'

# Button
def clicked():
    my_label['text'] = input.get()
    new_label.config(text="You've got it!")
    tkinter.Label(text='I got clicked').grid(row=2, column=1)
    print('I got clicked')

def clicked2():
    my_label['text'] = 'You were told not to click!'

button = tkinter.Button(text='Click Me', command=clicked)
button.grid(row=1, column=1)
button.config(padx=50, pady=30)

new_button = tkinter.Button(text="Don't Click Me", command=clicked2)
new_button.grid(row=0, column=2)

# Entry
input = tkinter.Entry(width=10)
input.grid(row=2, column=3)


tkinter.mainloop()
