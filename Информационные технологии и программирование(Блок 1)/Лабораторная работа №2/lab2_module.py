import math
import logging
def calc(x, y, a, b):
    if -4 < x <= 1 and y > -2:
        min = x ** y
        if min > math.e ** x:
            min = math.e ** x
        if min > a:
            min = a
        result = math.tan(x + y*x + a ** 2 * min) ** 2
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
    return result
