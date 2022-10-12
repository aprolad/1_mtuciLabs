import math
import logging
class lab2:
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.result = 0
    def branch1(self):
        min = self.x ** self.y
        if min > math.e ** self.x:
            min = math.e ** self.x
        if min > a:
            min = a
        self.result = math.tan(self.x + self.y * self.x + self.a ** 2 * min) ** 2
    def branch2(self):
        max = self.x + self.a ** 2
        if max < self.y:
            max = self.y
        min = self.y * math.sin(x)
        if min > self.a:
            min = self.a
        try:
            self.result = max / min
        except Exception as e:
            print("Деление на ноль!")
            logging.error(str(e))
            exit()
    def branch3(self):
        self.result = self.b + math.sin(math.fabs(math.e ** self.x)) ** 2
logging.basicConfig(filename="log.txt", level=logging.DEBUG)
x = float(input("Введите x "))
y = float(input("Введите y "))
a = float(input("Введите a "))
b = float(input("Введите b "))
lab = lab2(x, y, a, b)
if -4 < x <= 1 and y > -2:
    lab.branch1()
elif 1 < x <= 5 and -2 <= y < 8:
    lab.branch2()
else:
    lab.branch3()
t = lab.result
logging.info(str(t))
print("Результат программы: " + str(t))
try:
    with open("lab2result.txt", "a") as f:
        f.write("Результат работы программы: " + str(t) + "\n")
except Exception as e:
    logging.error(str(e))