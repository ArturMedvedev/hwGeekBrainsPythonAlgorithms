'''
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
'''

import random

# Генерируем массив.
SIZE = 20
MIN_ITM = -100
MAX_ITM = 99

array = [random.randint(MIN_ITM, MAX_ITM) for i in range(SIZE)]
print('Исходный массив:        ', array)

# Сортируем по убыванию пузырьком.
def sort_bubble(arr):
    n = 1
    while n < len(arr):
        for i in range(len(arr)-n):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        n += 1
    print('Отсортированный массив: ', arr)

sort_bubble(array)