from tkinter import *
from math import sqrt

#Functions
def clear():
    display.delete(0, END)

def backspace():
    math_expression = display.get()
    size = (len(math_expression))
    display.delete(size-1)

def calculate():
    try:
        math_expression = display.get()
        result = eval(math_expression)
        clear()
        display.insert(END, result)
    except:
        clear()
        display.insert(END, "ERROR")

def insert(valor):
    display.insert(END, valor)
def square_root():
    try:
        number = float(display.get())
        number_sqrt = sqrt(number)
        clear()
        display.insert(END, str(number_sqrt))
    except:
        clear()
        display.insert(END, "ERROR")

def percentage():
        try:
            math_expression = display.get()
            for op in ["+", "-", "*", "/"]:
                if op in math_expression:
                    base, perc = math_expression.split(op)
                    left = float(base)
                    right = float(perc)
                    if op in ["+", "-"]:
                        number_perc = left * right / 100
                    else:
                        number_perc = right / 100
                    new_exp = f"{base}{op}{number_perc}"
                    clear()
                    display.insert(END, new_exp)

        except:
            clear()
            display.insert(END, "ERROR")
        return

#---------------------------------------------
#Calculator Window
window = Tk()
window.title("Calculator")
window.geometry("200x300")
for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for i in range(6):
    window.grid_rowconfigure(i, weight=1)
window.bind("<Return>", lambda event: calculate())
window.bind("<BackSpace>", lambda event: backspace())

#--------------------------------------------
#Calculator Display
display = Entry(window)
display.config(font=("Arial", 24), justify="right")
display.grid(row=0, column=0, columnspan=4, pady = 10, ipady = 10, sticky = "nsew")

#---------------------------------------------
#Buttons
buttons = [
    ("C", 1, 0),
    ("7", 2, 0),
    ("4", 3, 0),
    ("1", 4, 0),
    ("0", 5, 0),
    ("sqrt", 1, 1),
    ("8", 2, 1),
    ("5", 3, 1),
    ("2", 4, 1),
    (".", 5, 1),
    ("%", 1, 2),
    ("9", 2, 2),
    ("6", 3, 2),
    ("3", 4, 2),
    ("=", 5, 2),
    ("<-", 1, 3),
    ("/", 2, 3),
    ("*", 3, 3),
    ("-", 4, 3),
    ("+", 5, 3)
]

#---------------------------------------------
# Create buttons
for text, row, column in buttons:
    if text == "C":
        comando = clear
    elif text == "=":
        comando = calculate
    elif text == "<-":
        comando = backspace
    elif text == "sqrt":
        comando = square_root
    elif text == "%":
        comando = percentage
    else:
        comando = lambda t=text: insert(t)

    button = Button(window, text= text, height = 2, command=comando)
    button.grid(row=row, column=column, sticky = "nsew")

#--------------------------------------------

window.mainloop()