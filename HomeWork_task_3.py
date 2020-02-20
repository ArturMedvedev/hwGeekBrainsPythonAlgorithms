'''
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
'''

s = input('Введите натуральное число: ')

'''
Решение через цикл.
'''
# a = ''
# for i in s:
#     a = i + a
# a = int(a)
# print(a, type(a))


'''
Решение рекурсивно. Блок-схема представлена по решению рекурсивно.
'''


def rev(count, new_num, old_list):
    if count == 0:
        return new_num
    new_str = old_list.pop()
    return rev((count - 1), (new_num + new_str), old_list)


new_number = int(rev(len(s), '', list(s)))
print(new_number, type(new_number))
