'''
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное
и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
'''

import timeit
import cProfile


# 1. С помощью "Решета Эратосфена".

def sieve(n):
    m = n * 20  # Определяем размер массива, в котором точно есть искомое число.
    sieve = [i for i in range(m)]
    sieve[1] = 0
    for i in range(2, m):
        if sieve[i] != 0:
            j = i + i
            while j < m:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    return res[n - 1]


print(timeit.timeit('sieve(100)', number=100, globals=globals()))  # 0.0403834
print(timeit.timeit('sieve(200)', number=100, globals=globals()))  # 0.0828359
print(timeit.timeit('sieve(300)', number=100, globals=globals()))  # 0.1369602
print(timeit.timeit('sieve(400)', number=100, globals=globals()))  # 0.17545859999999996
print(timeit.timeit('sieve(500)', number=100, globals=globals()))  # 0.22551930000000003

cProfile.run('sieve(250)')  # 1    0.001    0.001    0.001    0.001 HomeWork_task_2.py:14(sieve)
cProfile.run('sieve(500)')  # 1    0.002    0.002    0.002    0.002 HomeWork_task_2.py:14(sieve)
cProfile.run('sieve(1000)')  # 1    0.004    0.004    0.005    0.005 HomeWork_task_2.py:14(sieve)
cProfile.run('sieve(2000)')  # 1    0.008    0.008    0.009    0.009 HomeWork_task_2.py:14(sieve)

'''
Наблюдается линейная зависимость времени выполнения от объема массива.
'''

# 2. Без "Решета Эратосфена".

def prime(n):
    m = 3  # Первое проверяемое число.
    array = [2, ]  # Массив для записи проверяемых чисел.
    prime = [2, ]  # Массив для записи простых чисел.

    while len(prime) < n:  # Внешний цикл для нахождения простых чисел.
        spam = []
        for i in array:  # Цикл для последовательного деления текущего числа на все числа до него.
            if m % i != 0:
                spam.append(1)
            else:
                spam.append(0)
        if 0 not in spam:
            prime.append(m)
        array.append(m)
        m += 1

    return prime[n - 1]  # Возвращаем искомое число


print(timeit.timeit('prime(100)', number=100, globals=globals()))  # 1.0671274
print(timeit.timeit('prime(200)', number=100, globals=globals()))  # 5.4874304
print(timeit.timeit('prime(300)', number=100, globals=globals()))  # 14.642671800000002
print(timeit.timeit('prime(400)', number=100, globals=globals()))  # 28.0210091
print(timeit.timeit('prime(500)', number=100, globals=globals()))  # 47.77167440000001

cProfile.run('prime(250)')  # 1582    0.000    0.000    0.000    0.000 {built-in method builtins.len}
                            # 1252401    0.065    0.000    0.065    0.000 {method 'append' of 'list' objects}
cProfile.run('prime(500)')  # 3570    0.000    0.000    0.000    0.000 {built-in method builtins.len}
                            # 6374733    0.327    0.000    0.327    0.000 {method 'append' of 'list' objects}
cProfile.run('prime(1000)')  # 7918    0.001    0.000    0.001    0.000 {built-in method builtins.len}
                             # 31352319    1.604    0.000    1.604    0.000 {method 'append' of 'list' objects}
cProfile.run('prime(2000)')  # 17388    0.002    0.000    0.002    0.000 {built-in method builtins.len}
                             # 151181964    7.617    0.000    7.617    0.000 {method 'append' of 'list' objects}

'''
При увеличении входного параметра в 2 раза, время выполнения возрастает примерно в 6 раз.
Зависимость на глаз параболическая. Данный алгоритм полностью проигрывает "Решету Эратосфена".
Сомнительным плюсом данного алгоритма является возможность не определять заранее примерный размер
массива.
'''