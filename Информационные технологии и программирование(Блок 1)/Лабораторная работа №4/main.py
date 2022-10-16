from classModule import *
choice = None
lab = solver(0,0,0,0)
lab.__x
while choice != "0":
 print \
 ("""
 Меню
 0 - Выйти
 1 - Выполнить программу
 """)
 choice = input("Сделайте выбор ")
 print()
 if choice == "0":
    print("Заканчиваем работу")
 elif choice == "1":
    print("Введите исходные данные ")
    x = float(input("Введите x "))
    y = float(input("Введите y "))
    a = float(input("Введите a "))
    b = float(input("Введите b "))
    lab = solver(x, y, a, b)
    lab.solve()
    print("Результат вычислений: " + str(lab.result))
 else:
    print("Такого пункта в меню нет ", choice)
