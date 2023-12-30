# Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр. Отриманий результат повертається із функції.

# def multiply_elements(lst):
#     result = 1
#     for num in lst:
#         result *= num
#     return result
#
# num = [2,3,4,5]
# print("Отриманий результат який повертається із функції: ", multiply_elements(num))

# Напишіть функцію для знаходження мінімуму у списку цілих. Список передається як параметр. Отриманий результат повертається із функції.
def find_minimum(lst):
    if not lst:
        return None
    min_value = lst[0]
    for num in lst[1:]:
        if num < min_value:
            min_value = num
    return min_value

my_list = [5, 3, 9, 1, 7]
print("Отриманий результат який повертається із функції: ", find_minimum(my_list))