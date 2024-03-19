import tkinter as tk
import math 


def add_digit(operation, digit, input_l, label = None):
    match operation:
        case "add":
            curent = input_l.get() 
            input_l.delete(0, tk.END) 
            input_l.insert(0, curent + str(digit))
        case "erase":
            curent = input_l.get()
            input_l.delete(0, tk.END)  
            input_l.insert(0, curent[:-1])
        case "erase_all":
            curent = input_l.get()
            input_l.delete(0, tk.END) 
            label.config(text= f"Результат: ")


def calculate(input_l, label):
    curent = input_l.get()
    try:
        result = eval(curent) 
        label.config(text=f"Делить на ноль нельзя!" if error(result) else f"Результат: {result}")
    except ZeroDivisionError:
        label.config(text="Делить на ноль нельзя!")
    except SyntaxError:
        label.config(text="Результат: ")


def error(result):
    return result == float('inf') or result == float('-inf')
