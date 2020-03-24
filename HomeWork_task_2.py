'''
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
'''

import random

# Генерируем массив.
SIZE = 20
MIN_ITM = 0
MAX_ITM = 50

array = [round((MIN_ITM + (MAX_ITM - MIN_ITM) * random.random()), 2) for i in range(SIZE)]
print('Исходный массив:        ', array)


# Сортируем по возрастанию слиянием.
def sort_merge(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2  # Находим середину массива
    left = arr[:mid]  # Левая часть массива
    right = arr[mid:]  # Правая часть массива
    sort_merge(left)  # Рекурсивно разбиваем левую часть массива
    sort_merge(right)  # Рекурсивно разбиваем правую часть массива
    l, r, i = 0, 0, 0  # Начальные индексы для левой, правой части массива и самого массива
    while l < len(left) and r < len(right):  # Если сливаемые части одинаковы по длине
        if left[l] < right[r]:
            arr[i] = left[l]
            l += 1
        else:
            arr[i] = right[r]
            r += 1
        i += 1
    while l < len(left):  # Если левая часть длиннее
        arr[i] = left[l]
        l += 1
        i += 1
    while r < len(right):  # Если правая часть длиннее
        arr[i] = right[r]
        r += 1
        i += 1
    return arr


sort_merge(array)
print('Отсортированный массив: ', array)