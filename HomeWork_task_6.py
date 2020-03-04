'''
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
'''

# 1. Генерируем исходный массив.

import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# 2. Тело задачи.

max_num = min_num = array[0]  # Задаем начальные значения макс. и мин. элементам.
max_index = min_index = 0  # Задаем начальные значения индексов макс. и мин. элемента.

for idx, i in enumerate(array):  # Цикл определения макс. и мин. элементов и сразу их индексов.
    if max_num <= i: # Условие определение последнего максимального элемента.
        max_num = i
        max_index = idx
    elif min_num > i: # Условие определение первого минимального элемента.
        min_num = i
        min_index = idx

total = 0  # Задаем переменную для суммы.

if max_index > min_index:  # Если максимальный элемент после минимального.
    for i in array[min_index + 1:max_index]:  # Цикл нахождения суммы.
        total += i
elif max_index < min_index:  # Если минимальный элемент после максимального.
    for i in array[max_index + 1:min_index]:  # Цикл нахождения суммы.
        total += i

print('Cуммa элементов, находящихся между минимальным и максимальным элементами =', total)
