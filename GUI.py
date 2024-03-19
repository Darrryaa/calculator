import tkinter as tk
from calc import *


def GUI():
    root = tk.Tk()
    root.title("Калькулятор")

    root.geometry('300x500')
    input_l = tk.Entry(root, width=30)
    input_l.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
    label = tk.Label(root, text="Результат: ")
    label.grid(row=1, column=1, columnspan=4, padx=10, pady=10)
    
    # 1
    btn = tk.Button(root, text=str(1), command=lambda digit=1: add_digit("add", digit, input_l), height=3, width=5)
    btn.grid(row=2, column=0, padx=10,
             pady=10) 

    # 2
    btn = tk.Button(root, text=str(2), command=lambda digit=2: add_digit("add", digit, input_l), height=3, width=5)
    btn.grid(row=2, column=1, padx=10, pady=10)

    # 3
    btn = tk.Button(root, text=str(3), command=lambda digit=3: add_digit("add", digit, input_l), height=3, width=5)
    btn.grid(row=2, column=2, padx=10, pady=10)

    # 4
    btn = tk.Button(root, text=str(4), command=lambda digit=4: add_digit("add", digit, input_l), height=3, width=5)
    btn.grid(row=3, column=0, padx=10, pady=10)

    # 5
    btn = tk.Button(root, text=str(5), command=lambda digit=5: add_digit("add", digit, input_l), height=3, width=5)
    btn.grid(row=3, column=1, padx=10, pady=10)

    # 6
    btn = tk.Button(root, text=str(6), command=lambda digit=6: add_digit("add", digit, input_l), height=3, width=5)
    btn.grid(row=3, column=2, padx=10, pady=10)

    # 7
    btn = tk.Button(root, text=str(7), command=lambda digit=7: add_digit("add", digit, input_l), height=3, width=5)
    btn.grid(row=4, column=0, padx=10, pady=10)

    # 8
    btn = tk.Button(root, text=str(8), command=lambda digit=8: add_digit("add", digit, input_l), height=3, width=5)
    btn.grid(row=4, column=1, padx=10, pady=10)

    # 9
    btn = tk.Button(root, text=str(9), command=lambda digit=9: add_digit("add", digit, input_l), height=3, width=5)
    btn.grid(row=4, column=2, padx=10, pady=10)

    # 0
    btn = tk.Button(root, text=str(0), command=lambda digit=0: add_digit("add", digit, input_l), height=3, width=5)
    btn.grid(row=5, column=1, padx=10, pady=10)

    # +
    btn = tk.Button(root, text="+", command=lambda digit="+": add_digit("add", digit, input_l), height=3, width=5)
    btn.grid(row=2, column=4, padx=10, pady=10)

    # -
    btn = tk.Button(root, text="-", command=lambda digit="-": add_digit("add", digit, input_l), height=3, width=5)
    btn.grid(row=3, column=4, padx=10, pady=10)

    # /
    btn = tk.Button(root, text="/", command=lambda digit="/": add_digit("add", digit, input_l), height=3, width=5)
    btn.grid(row=4, column=4, padx=10, pady=10)

    # *
    btn = tk.Button(root, text="*", command=lambda digit="*": add_digit("add", digit, input_l), height=3, width=5)
    btn.grid(row=5, column=4, padx=10, pady=10)

    # =
    btn = tk.Button(root, text="=", command=lambda input_ll=input_l: calculate(input_ll, label), height=3, width=5)
    btn.grid(row=6, column=4, padx=10, pady=10)

    # <-
    btn = tk.Button(root, text="<-", command=lambda input_ll=input_l: add_digit("erase", 0, input_l), height=3, width=5)
    btn.grid(row=6, column=3, padx=10, pady=10)
