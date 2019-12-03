# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

a = int(input('Enter the month number from 1 to 12\n'))

if a == 1 or a == 2 or a == 12:  # определяем сезон
    print('Winter')
elif a == 3 or a == 4 or a == 5:
    print('Spring')
elif a == 6 or a == 7 or a == 8:
    print('Summer')
elif a == 9 or a == 10 or a == 11:
    print('Autumn')
else:
    print('Error')

month_dict = {1: 'January',
              2: 'February',
              3: 'March',
              4: 'April',
              5: 'May',
              6: 'June',
              7: 'Jule',
              8: 'August',
              9: 'September',
              10: 'October',
              11: 'November',
              12: 'December'}

print(f"It is {month_dict[a]}")

# функция берет значение из словаря с ключом,
# где ключ - это введенный пользователем номер месяца
