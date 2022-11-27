import math
from tkinter import *
import logging

class Application(Frame):
    def __init__(self, fr):
        super(Application, self).__init__(fr)
        self.grid()
        self.widget()
    # Создаем метод для нахождения значения функции
    def func(self):
        x = float(self.textbox1.get())
        y = float(self.textbox2.get())
        a = float(self.textbox3.get())
        b = float(self.textbox4.get())
        result = 0
        if -4 < x <= 1 and y > -2:
            min = x ** y
            if min > math.e ** x:
                min = math.e ** x
            if min > a:
                min = a
            result = math.tan(x + y * x + a ** 2 * min) ** 2
        elif 1 < x <= 5 and -2 <= y < 8:
            max = x + a ** 2
            if max < y:
                max = y
            min = y * math.sin(x)
            if min > a:
                min = a
            try:
                result = max / min
            except Exception as e:
                print("Деление на ноль!")
                logging.error(str(e))
                exit()
        else:
            result = b + math.sin(math.fabs(math.e ** x)) ** 2
        self.textbox5.insert(0.0, result)
    # Создаем виджеты на форме
    def widget(self):
        self.lbl1 = Label(self, text="Введите число x", font=("Times New Roman", 16), fg="blue")
        self.lbl1.grid(row=0, column=0)
        self.textbox1 = Entry(self, width=67, font=("Times New Roman", 16))
        self.textbox1.grid(row=1, column=0)
        # ----------------------------------------
        self.lbl2 = Label(self, text="Введите значение y", font=("Times New Roman", 16), fg="blue")
        self.lbl2.grid(row=2, column=0)
        self.textbox2 = Entry(self, width=67, font=("Times New Roman", 16))
        self.textbox2.grid(row=3, column=0)
        # ----------------------------------------
        self.lbl3 = Label(self, text="Введите значение a", font=("Times New Roman", 16), fg="blue")
        self.lbl3.grid(row=4, column=0)
        self.textbox3 = Entry(self, width=67, font=("Times New Roman", 16))
        self.textbox3.grid(row=5, column=0)
        # ----------------------------------------
        self.lbl4 = Label(self, text="Введите значение b", font=("Times New Roman", 16), fg="blue")
        self.lbl4.grid(row=6, column=0)
        self.textbox4 = Entry(self, width=67, font=("Times New Roman", 16))
        self.textbox4.grid(row=7, column=0)
        # ----------------------------------------
        self.btn = Button(self, font=("Times New Roman", 14, "bold"), fg="red")
        self.btn["text"] = "Вычислить функцию"
        self.btn["command"] = self.func
        self.btn["width"] = 20
        self.btn["height"] = 2
        self.btn.grid(row=8, column=0)
        self.lbl5 = Label(self, text="Значение функции", font=("Times New Roman", 14), fg="green")
        self.lbl5.grid(row=9, column=0)
        self.textbox5 = Text(self, width=30, height=1, font=("Times New Roman", 14))
        self.textbox5.grid(row=10, column=0)
root = Tk()
root.title("Лабораторная работа №8")
root.geometry("740x550")
app = Application(root)
root.mainloop()
