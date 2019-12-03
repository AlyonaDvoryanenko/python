# Задание 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

# Решение:

user_number = int(input('Введите число n\n'))  # запрашиваю число n
var1 = str(user_number)  # делаю его строкой
var2 = var1 + var1  # склеиваю
var3 = var1 + var1 + var1  # склеиваю
user_number_sum = int(user_number) + int(var2) + int(var3)  # нашла сумму по формуле
print('Сумма чисел n+nn+nnn: ', user_number_sum)  # вывела на экран
