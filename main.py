# # 1. Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр. Отриманий результат повертається із функції.
#
# def multiply_elements(lst):
#     result = 1
#     for num in lst:
#         result *= num
#     return result
#
# num = [2,3,4,5]
# print("Отриманий результат який повертається із функції: ", multiply_elements(num))
#
# # 2. Напишіть функцію для знаходження мінімуму у списку цілих. Список передається як параметр. Отриманий результат повертається із функції.
# def find_minimum(lst):
#     if not lst:
#         return None
#     min_value = lst[0]
#     for num in lst[1:]:
#         if num < min_value:
#             min_value = num
#     return min_value
#
# num2 = [5, 3, 9, 1, 7]
# print("Отриманий результат який повертається із функції: ", find_minimum(num2))
#
# # 3. Напишіть функцію, яка визначає кількість простих чисел у списку цілих. Список передається як параметр. Отриманий результат повертається із функції.
#
# def count_primes(lst):
#     def is_prime(n):
#         if n < 2:
#             return False
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True
#
#     count = 0
#     for num in lst:
#         if is_prime(num):
#             count += 1
#     return count
#
# num3 = [2, 3, 4, 5, 6, 7, 8, 9]
# print("Отриманий результат повертається із функції: ",count_primes(num3))

# # 4.Напишіть функцію, яка видаляє зі списку ціле задане число. З функції потрібно повернути кількість видаленних елементів.
#
# def remove_element(lst, target):
#     count_removed = lst.count(target)
#     lst = [num for num in lst if num != target]
#     return count_removed
#
# num4 = [1, 2, 3, 4, 2, 5, 2]
# target_number = 2
# print("Кількість видаленних елементів: ",remove_element(num4, target_number))

# 5.Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.

# def merge_lists(list1, list2):
#     return list1 + list2
#
# list_num1 = [1, 2, 3]
# list_num2 = [4, 5, 6]
# print("Два списки: ",merge_lists(list_num1, list_num2))
