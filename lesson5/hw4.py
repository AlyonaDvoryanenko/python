# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_f = open("numbers", "r")
content = my_f.readlines()
print(content)

russian_dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('numbers', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(russian_dic[i[0]] + '  ' + i[1])
    print(new_file)

with open('numbers_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)
