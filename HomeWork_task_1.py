'''
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках
домашнего задания первых трех уроков.

Урок 3. Задание №3.
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

import timeit
import cProfile
import random


# 0. Генератор массива.

def lst_gen(SIZE):
    MIN_ITEM = 0
    MAX_ITEM = 1000
    return [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


# 1. Цикл. Перебор массива, определение индексов, замена.

def func_loop(SIZE):
    array = lst_gen(SIZE)
    max_num = min_num = array[0]  # Задаем начальные значения макс. и мин. элементам.

    for i in range(len(array) - 1):  # Цикл определения макс. и мин. элементов.
        if max_num < array[i + 1]:
            max_num = array[i + 1]
        elif min_num > array[i + 1]:
            min_num = array[i + 1]

    min_index = array.index(min_num)  # Определяем индекс минимального элемента.
    max_index = array.index(max_num)  # Определяем индекс максимального элемента.

    array[min_index], array[max_index] = array[max_index], array[min_index]  # Меняем местами макс. и мин. элемент.


print(timeit.timeit('func_loop(100)', number=1000, globals=globals()))  # 0.0720661
print(timeit.timeit('func_loop(1000)', number=1000, globals=globals()))  # 0.7452262000000001
print(timeit.timeit('func_loop(10000)', number=1000, globals=globals()))  # 7.303023199999999
print(timeit.timeit('func_loop(100000)', number=1000, globals=globals()))  # 73.50031659999999

cProfile.run('func_loop(100000)')  # 1    0.018    0.018    0.125    0.125 HomeWork_task_1.py:16(<listcomp>)
                                   # 2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
cProfile.run('func_loop(1000000)')  # 1    0.195    0.195    1.265    1.265 HomeWork_task_1.py:16(<listcomp>)
                                    # 2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
cProfile.run('func_loop(10000000)')  # 1    1.948    1.948   12.642   12.642 HomeWork_task_1.py:16(<listcomp>)
                                     # 2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
cProfile.run('func_loop(100000000)')  # 1   19.438   19.438  126.140  126.140 HomeWork_task_1.py:16(<listcomp>)
                                      # 2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

'''
Наблюдается линейная зависимость времени выполнения от объема массива. Подавляющее кол-во времени
уходит на создание массива. Поиск индексов в массиве происходит "мгновенно".
'''

# 2. Цикл с enumerate, определяем индексы при первом прохождении цикла.

def func_enum(SIZE):
    array = lst_gen(SIZE)
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


print(timeit.timeit('func_enum(100)', number=1000, globals=globals()))  # 0.0681317
print(timeit.timeit('func_enum(1000)', number=1000, globals=globals()))  # 0.6606199
print(timeit.timeit('func_enum(10000)', number=1000, globals=globals()))  # 6.655111600000001
print(timeit.timeit('func_enum(100000)', number=1000, globals=globals()))  # 66.89259779999999

cProfile.run('func_enum(100000)')  # 1    0.017    0.017    0.125    0.125 HomeWork_task_1.py:16(<listcomp>)
                                   # 1    0.005    0.005    0.130    0.130 HomeWork_task_1.py:58(func_enum)
cProfile.run('func_enum(1000000)')  # 1    0.187    0.187    1.263    1.263 HomeWork_task_1.py:16(<listcomp>)
                                    # 1    0.052    0.052    1.315    1.315 HomeWork_task_1.py:58(func_enum)
cProfile.run('func_enum(10000000)')  #  1    1.882    1.882   12.627   12.627 HomeWork_task_1.py:16(<listcomp>)
                                     # 1    0.524    0.524   13.151   13.151 HomeWork_task_1.py:58(func_enum)
cProfile.run('func_enum(100000000)')  # 1   18.824   18.824  126.388  126.388 HomeWork_task_1.py:16(<listcomp>)
                                      # 1    5.253    5.253  131.641  131.641 HomeWork_task_1.py:58(func_enum)

'''
Наблюдается линейная зависимость времени выполнения от объема массива. Подавляющее кол-во времени
уходит на создание массива.
'''

# 3. Встроенные методы, функции.

def func_methods(SIZE):
    array = lst_gen(SIZE)
    max_index = array.index(max(array))  # Определяем индекс максимума.
    min_index = array.index(min(array))  # Определяем индекс минимума.
    array[min_index], array[max_index] = array[max_index], array[min_index]  # Меняем местами макс. и мин. элемент.


print(timeit.timeit('func_methods(100)', number=1000, globals=globals()))  # 0.0659315
print(timeit.timeit('func_methods(1000)', number=1000, globals=globals()))  # 0.6519067000000001
print(timeit.timeit('func_methods(10000)', number=1000, globals=globals()))  # 6.323073600000001
print(timeit.timeit('func_methods(100000)', number=1000, globals=globals()))  # 63.4412711

cProfile.run('func_methods(100000)')  # 1    0.017    0.017    0.124    0.124 HomeWork_task_1.py:16(<listcomp>)
                                      # 1    0.000    0.000    0.125    0.125 HomeWork_task_1.py:95(func_methods)
                                      # 2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
cProfile.run('func_methods(1000000)')  # 1    0.191    0.191    1.275    1.275 HomeWork_task_1.py:16(<listcomp>)
                                       # 1    0.000    0.000    1.290    1.290 HomeWork_task_1.py:95(func_methods)
                                       # 2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
cProfile.run('func_methods(10000000)')  # 1    1.888    1.888   12.602   12.602 HomeWork_task_1.py:16(<listcomp>)
                                        # 1    0.000    0.000   12.746   12.746 HomeWork_task_1.py:95(func_methods)
                                        # 2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
cProfile.run('func_methods(100000000)')  # 1   18.978   18.978  126.277  126.277 HomeWork_task_1.py:16(<listcomp>)
                                         # 1    0.000    0.000  127.748  127.748 HomeWork_task_1.py:95(func_methods)
                                         # 2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

'''
Наблюдается линейная зависимость времени выполнения от объема массива. Подавляющее кол-во времени
уходит на создание массива. Поиск индексов в массиве происходит "мгновенно".
Вариант №3 самый быстрый и в плане исполнения, и в плане написания кода.
Но в целом, походу, неудачный пример задачи выбран.
'''