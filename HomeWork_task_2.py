'''
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''

from collections import deque

template = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
            'D': 13, 'E': 14, 'F': 15, }  # Шаблонный словарь.

num_1 = deque((input('Введите первое число: ')).upper())  # Очередь для ввода первого числа.
num_2 = deque((input('Введите второе число: ')).upper())  # Очередь для ввода второго числа.
answer = deque()  # Очередь для ответа.
print(num_1, num_2, sep='\n')  # Проверка на сохранение введенных чисел согласно условиям задачи.
num_1.reverse()  # Реверс первого числа для сложения с меньшего разряда.
num_2.reverse()  # Реверс второго числа для сложения с меньшего разряда.

if len(num_1) != len(num_2):  # Цикл выравнивания длины чисел, чтобы избежать ошибки отсутствия ключа.
    if len(num_1) < len(num_2):
        num_1, num_2 = num_2, num_1
    for _ in range(len(num_1) - len(num_2)):
        num_2.append('0')

limit = 0  # Переменная для "1 в уме".
for i in range(len(num_1)):  # Цикл сложения.
    if template[num_1[i]] + template[num_2[i]] + limit >= 16:  # Проверка разрядности ответа.
        sum = template[num_1[i]] + template[num_2[i]] + limit - 16
        limit = 1
    else:
        sum = template[num_1[i]] + template[num_2[i]] + limit
        limit = 0
    for key, values in template.items():  # Цикл для определения ключа из шаблона по значению.
        if sum == values:
            answer.appendleft(key)  # Формируем очередь с ответом.

answer_str = ''  # Преобразуем очередь для ответа в строчном виде.
for _ in answer:
    answer_str += _
print('Ответ: ' + answer_str)
