square = []

for x in range(1,6):
    square.append(x ** 2)
print(square)

#list comprehension - print square
square_comp = [x ** 2 for x in range(1,6)]
print(square_comp)

#even numbers
even_numbers = [x for x in range(1,10+1) if x % 2 == 0]
print(even_numbers)

#string
letters = [ch.upper() for ch in "helloo"]
print(letters)
