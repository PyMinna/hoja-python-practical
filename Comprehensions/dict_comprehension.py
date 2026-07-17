#square numbers as key value pairs
square_num = {x : x**2 for x in range(1,6)}
print(square_num)

#even numbers square
even_square = {x : x**2 for x in range(1,8) if x % 2 == 0}
print(even_square)