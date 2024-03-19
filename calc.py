import tkinter as tk
import math

def add_digit(operation, digit, input_l):
    match operation:
        case "add":
            curent = input_l.get() 
            input_l.delete(0, tk.END) 
            input_l.insert(0, curent + str(digit)) 
        case "erase":
            curent = input_l.get()
            input_l.delete(0, tk.END) 
            input_l.insert(0, curent[:-1])

def calculate(input_l, label):
    current = input_l.get()
    try:
        result = eval(current) 
        label.config(text=f"Делить на ноль нельзя!" if error(result) else f"Результат: {result}")
    except ZeroDivisionError:
        label.config(text="Делить на ноль нельзя!")


def error(result):
    return result == float('inf') or result == float('-inf')
