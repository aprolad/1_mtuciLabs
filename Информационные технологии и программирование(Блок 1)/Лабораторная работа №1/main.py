import math
class lab1:
    def __init__(self, x, y):
        self.output = (1 - math.e**(x*y))/(0.7 * math.log10(math.fabs(1 - x**2)))
x = float(input("Введите x "))
y = float(input("Введите y "))
result = lab1(x, y).output
c = math.ceil(result)
t = math.trunc(result)
f = math.floor(result)
r = round(result, 3)
print("Результат работы программы: " + str(result))
print("Округленный до большего результат: " + str(c))
print("Усеченный до целого результат: " + str(t))
print("Округленный до меньшего результат: " + str(f))
print("Округленный с точностью до трех знаков результат: " + str(r))
f = open("lab1result.txt", "w")
f.write("Результат работы программы: " + str(result) + "\n")
f.write("Округленный до большего результат: " + str(math.ceil(result)))
f.write("\nУсеченный до целого результат: " + str(math.trunc(result)))
f.write("\nОкругленный до меньшего результат: " + str(math.floor(result)))
f.write("\nОкругленный с точностью до трех знаков результат: " + str(round(result, 3)))
f.close()
