# Задание 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

# Решение:

user_time = int(input('Введите время в секундах\n'))  # запросила время у пользователя число

hours = (user_time / 3600)  # перевела в часы
whole_hours = round(hours)  # округлила

minutes = (hours - int(hours)) * 60  # перевела в минуты
whole_minutes = round(minutes)  # округлила

seconds = (minutes - int(minutes)) * 100  # перевела в секунды
whole_seconds = round(seconds)  # округлила

full_data = f'{whole_hours} : {whole_minutes} : {whole_seconds}'  # форматирование строки
print('Точное время чч:мм:сс ', full_data)  # вывела на экран
