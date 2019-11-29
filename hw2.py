# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# Решение:

user_name = input('Введите ваше имя ')
user_surname = input('Введите вашу фамилию ')
user_birth_date = int(input('Введите ваш год рождения '))
user_city = input('Введите ваш город проживания ')
user_email = input('Введите ваш email ')
user_phone = int(input('Введите ваш номер телефона '))

var1 = user_name
var2 = user_surname
var3 = user_birth_date
var4 = user_city
var5 = user_email
var6 = user_phone


def user_func(var1, var2, var3, var4, var5, var6):
    print(
        f"Имя: {var1}, Фамилия: {var2}, Год рождения: {var3}, Город проживания: {var4}, email: {var5}, Номер телефона: {var6}")


user_func(var1=user_name, var2=user_surname, var3=user_birth_date,
          var4=user_city, var5=user_email, var6=user_phone)
