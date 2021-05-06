import tkinter as tk


def onclick():
    k = 1.609344
    if radio_state.get():
        k = 1 / k
    try:
        result = round(float(entry.get()) * k, 3)
        if check_state.get():
            result = round(result)
        result_label['text'] = result
        error_label['text'] = ''
    except ValueError:
        error_label['text'] = 'Error'


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

check_state = tk.IntVar()
roundbox = tk.Checkbutton(text='round', variable=check_state)
roundbox.grid(row=3, column=0)

equal_label = tk.Label(text='is equal to')
equal_label.grid(row=2, column=0)
label1 = tk.Label(text='Miles')
label1.grid(row=1, column=2)
label2 = tk.Label(text='Km')
label2.grid(row=2, column=2)
result_label = tk.Label(text='0')
result_label.grid(row=2, column=1)
error_label = tk.Label()
error_label.grid(row=4, column=1)

entry = tk.Entry(width=10)
# entry.insert(index=0, string='0')
entry.focus()
entry.grid(row=1, column=1)

btn = tk.Button(text='Calculate')
btn.config(command=onclick)
btn.grid(row=3, column=1)

window.mainloop()
