import math
class solver:
    def __init__(self, x, y, a, b):
        self.__x = x
        self.__y = y
        self.__a = a
        self.__b = b
        self.result = 0
    def __branch1(self):
        min = self.__x ** self.__y
        if min > math.e ** self.__x:
            min = math.e ** self.__x
        if min > self.__a:
            min = self.__a
        self.result = math.tan(self.__x + self.__y * self.__x + self.__a ** 2 * min) ** 2
    def __branch2(self):
        max = self.__x + self.__a ** 2
        if max < self.__y:
            max = self.__y
        min = self.__y * math.sin(self.__x)
        if min > self.__a:
            min = self.__a
        try:
            self.result = max / min
        except Exception as e:
            print("Деление на ноль!")
            exit()
    def __branch3(self):
        self.result = self.__b + math.sin(math.fabs(math.e ** self.__x)) ** 2
    def solve(self):
        if -4 < self.__x <= 1 and self.__y > -2:
            self.__branch1()
        elif 1 < self.__x <= 5 and -2 <= self.__y < 8:
            self.__branch2()
        else:
            self.__branch3()
