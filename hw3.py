# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

# Решение:

# Функция может принимать неопределенное число позиционных параметров.
# В этом случае при описании функции используется конструкция *args.

var1 = [10, 20, 30]

a = var1
a.sort()
a.reverse()

var_max1 = a[0]

print(var_max1)

var_max2 = a[1]

print(var_max2)


def my_func(a):
    return var_max1 + var_max2


print(my_func(a))



