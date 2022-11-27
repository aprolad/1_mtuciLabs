from lab2_module import *


logging.basicConfig(filename="log.txt", level=logging.DEBUG)
x = float(input("Введите x "))
y = float(input("Введите y "))
a = float(input("Введите a "))
b = float(input("Введите b "))
t = calc(x, y, a, b)
logging.info(str(t))
print("Результат программы: " + str(t))
try:
    with open("lab2result.txt", "a") as f:
        f.write("Результат работы программы: " + str(t) + "\n")
except Exception as e:
    logging.error(str(e))
