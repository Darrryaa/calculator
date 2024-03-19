import tkinter as tk
import math 

# operation - будет принимать два значения - добавить символ и стереть символ)
def add_digit(operation, digit, input_l):
    match operation:
        case "add":
            curent = input_l.get() #Здесь мы считываем то что лежит в строке
            input_l.delete(0, tk.END) #Очищаем полностью поле input для предотвращения дублирования информации
            input_l.insert(0, curent + str(digit)) #Мы добавляем ту строку которую получили и к ней добавляем число которое нажал пользователь
        case "erase":
            curent = input_l.get()
            input_l.delete(0, tk.END) # tk.END - функция позволяющая удалить все что внутри инпута
            input_l.insert(0, curent[:-1])

def calculate(input_l, label):

    curent = input_l.get()
    result = eval(curent) #eval - сделать из строки выражение и посичтать его значение
    boleve = error(result)
    label.config(text= f"Делить на ноль нельзя!" if boleve else f"Результат: {result}")


def error(result):
    return result == float('inf') or result == float('-inf')