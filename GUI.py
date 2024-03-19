import tkinter as tk
from calc import *


def GUI():
    # Создаем объект класса, с помощью конструктора, который позволяет задать начальные значения
    # и в последующем использовать объект для внесения новых кнопочек, полей, названия, размеров и т.д.
    root = tk.Tk()
    root.title("Калькулятор")

    root.geometry('300x500')
    # .grid(row=0, column=0, columnspan=4)
    # Лямбда функция можеть иметь любое количество аргументов, но может быть только одно выражение, выражение вычисляется и возвращается.

    # лямбда функция в этом примере нужна для задания точного числа с кнопки и запуска команды по нажатию на кнопку,
    # без нее программа думает что кнопка всегда нажата, для того чтобы пользователь случайно не поломал логику
    # tk.Button - создает виджет кнопки (куда мы хотим поместить кнопку, что будет написано на кнопке, что кнопка должна запустить при нажатии)
    #row отвечает за координату по х, column отвечает за координату у
    # Виджет для ввода выражения
    input_l = tk.Entry(root, width=30)
    # columnspan - мы говорим что инпут будет занимать 4 столбца
    input_l.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

    # Виджет для отображения результата
    # Текстовое поле в котором мы отображаем
    label = tk.Label(root, text="Результат: ")
    label.grid(row=1, column=1, columnspan=4, padx=10, pady=10)

    # 1
    btn = tk.Button(root, text=str(1), command=lambda digit=1: add_digit("add", digit, input_l), height=3, width=5)
    btn.grid(row=2, column=0, padx=10,
             pady=10)  # нужна для создания сетки в приложении и размежения в ячейки сетки виджетов (засунуть кнопку в свою ячейку)

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
