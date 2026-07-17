#set comprehension
numbers = [1,2,2,3,4,3,5,4,4,6,2]
unique_numbers = {x ** 2 for x in numbers}
print(unique_numbers)

even_num = {x for x in numbers if x % 2 == 0}
print(even_num)

even_num = {x for x in range(1,11) if x % 2 == 0}
print(even_num)