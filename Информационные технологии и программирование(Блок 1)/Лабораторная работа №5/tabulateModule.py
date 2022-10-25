from calcModule import *
def tabulate(a, b, h):
    sum = 0
    x = a
    n = round((b - a)/h) + 1
    for i in range(1, n+1):
        temp = calc(x)
        sum += temp
        print("x= ", '{0:.2f}'.format(x), " y = ", '{0:.3f}'.format(temp))
        x += h
    avg = sum/n
    print("Среднее значение функции на промежутке ", avg)
