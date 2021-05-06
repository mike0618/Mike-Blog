import tkinter as tk


def onclick():
    k = 1.609344
    if radio_state.get():
        k = 1 / k
    try:
        label3['text'] = round(float(entry.get()) * k, 3)
    except ValueError:
        label4['text'] = 'Error'


def onradio():
    if radio_state.get():
        label1['text'] = 'Km'
        label2['text'] = 'Miles'
    else:
        label2['text'] = 'Km'
        label1['text'] = 'Miles'


window = tk.Tk()
window.title("Miles/Km Converter")
window.config(padx=30, pady=20)

radio_state = tk.IntVar()
rb1 = tk.Radiobutton(text='Miles to Km', value=0, variable=radio_state, command=onradio)
rb2 = tk.Radiobutton(text='Km to Miles', value=1, variable=radio_state, command=onradio)
rb1.grid(row=0, column=0)
rb2.grid(row=0, column=1)

label0 = tk.Label(text='is equal to')
label0.grid(row=2, column=0)
label1 = tk.Label(text='Miles')
label1.grid(row=1, column=2)
label2 = tk.Label(text='Km')
label2.grid(row=2, column=2)
label3 = tk.Label(text='0')
label3.grid(row=2, column=1)
label4 = tk.Label()
label4.grid(row=4, column=1)

entry = tk.Entry(width=10)
entry.insert(index=0, string='0')
entry.grid(row=1, column=1)

btn = tk.Button(text='Calculate')
btn.config(command=onclick)
btn.grid(row=3, column=1)

window.mainloop()
