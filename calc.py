import tkinter as tk
import math
import ru_local as ru


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
            label.config(text=(f'{ru.Result}'))


def calculate(input_l, label):
    curent = input_l.get()
    try:
        result = eval(curent)
        label.config(text=(f'{ru.You_can_not_divide_by_zero}') if error(result) else f'{ru.Result} {result}')
    except ZeroDivisionError:
        label.config(text=(f'{ru.You_can_not_divide_by_zero}'))
    except SyntaxError:
        label.config(text=(f'{ru.Result}'))


def error(result):
    return result == float('inf') or result == float('-inf')