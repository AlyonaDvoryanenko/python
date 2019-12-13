# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

my_file = open('salary')
content = my_file.read()
print(f'Содержание файла:\n{content}')

with open('salary', 'r') as my_file:
    sal = []
    less_twenty = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            less_twenty.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20000 {less_twenty}, средний оклад {sum(map(int, sal)) / len(sal)}')

