'''
Задание №3 из урока №2.
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
'''

import sys

# Вариант решения рекурсивно.
s = '3486'


def rev(count, new_num, old_list):
    if count == 0:
        return new_num
    new_str = old_list.pop()

    def func_var():  # Выводим переменные функции в глобальные, чтобы функция подсчета памяти их увидела.
        global q
        global x
        global y
        global z
        q = count
        x = new_num
        y = old_list
        z = new_str

    func_var()
    return rev((count - 1), (new_num + new_str), old_list)


new_number = int(rev(len(s), '', list(s)))
new_number = int(new_number)
print(new_number, type(new_number))

# Функция. Память под переменные.

def mem_sum(array):
    answer = 0  # Переменная для формирования ответа.
    for itm in array:
        answer += sys.getsizeof(itm)
    return answer

arr = [s, q, x, y, z, new_number]  # Ручками формируем список задействованных переменных.
print('Всего под переменные задействовано памяти: ', mem_sum(arr), 'байт')
'''
Всего под переменные задействовано памяти:  267 байт
Win x64
3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]

Это довольно прожорливый по памяти вариант решения.
'''