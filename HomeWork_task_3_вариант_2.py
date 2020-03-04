'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
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
    if max_num < i:
        max_num = i
        max_index = idx
    elif min_num > i:
        min_num = i
        min_index = idx

array[min_index], array[max_index] = array[max_index], array[min_index]  # Меняем местами макс. и мин. элемент.

print(array)
