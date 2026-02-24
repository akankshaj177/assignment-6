from tkinter import *

def click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

root = Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry = Entry(root, font=("Arial", 20), borderwidth=5, relief=RIDGE, justify="right")
entry.pack(fill=BOTH, ipadx=8, pady=10, padx=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

frame = Frame(root)
frame.pack()

for (text, row, col) in buttons:
    if text == "=":
        btn = Button(frame, text=text, width=5, height=2,
                     command=calculate)
    else:
        btn = Button(frame, text=text, width=5, height=2,
                     command=lambda t=text: click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

clear_btn = Button(root, text="Clear", width=20, height=2, command=clear)
clear_btn.pack(pady=10)

root.mainloop()
