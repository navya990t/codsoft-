import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error"

def evaluate_expression(expression):
    try:
        return eval(expression)
    except ZeroDivisionError:
        return "Error"
    except Exception as e:
        return "Error"

def button_click(value):
    if value == "C":
        entry.delete(0, tk.END)
    elif value == "=":
        expression = entry.get()
        result = evaluate_expression(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    else:
        entry.insert(tk.END, value)

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font=('Arial', 18), borderwidth=5, relief=tk.RIDGE)
entry.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0

for button in buttons:
    action = lambda x=button: button_click(x)
    tk.Button(root, text=button, width=7, height=3, command=action).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
