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

for i in range(len(array) - 1):  # Цикл определения макс. и мин. элементов.
    if max_num < array[i + 1]:
        max_num = array[i + 1]
    elif min_num > array[i + 1]:
        min_num = array[i + 1]

min_index = array.index(min_num)  # Определяем индекс минимального элемента.
max_index = array.index(max_num)  # Определяем индекс максимального элемента.

array[min_index], array[max_index] = array[max_index], array[min_index]  # Меняем местами макс. и мин. элемент.

print(array)
