# Реализовать рекурсивную функцию нарезания прямоугольника с заданными
# пользователем сторонами a и b на квадраты с наибольшей возможной на
# каждом этапе стороной. Вывести длины ребер получаемых квадратов и
# кол-во полученных квадратов.

a = int(input("Длина:  "))
b = int(input("Ширина: "))
area = a * b


def myFun(area):

    if area == 0:
        raise StopIteration
    while(area):
        for i in range(area, 0, -1):
            if i * i <= area:
                area -= i * i
                yield i
                break
        myFun(area)


result = list(myFun(area))
print(result)

