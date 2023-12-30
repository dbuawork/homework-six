def multiply_elements(lst):
    result = 1
    for num in lst:
        result *= num
    return result

num = [2,3,4,5]
print("Отриманий результат який повертається із функції: ", multiply_elements(num))
