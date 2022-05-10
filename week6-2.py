list_a = [[[1, 2, 3]], [3.2, 32, 1, 5]]
list_a_reverse = list(reversed(list_a))
print(list_a)
print(list_a_reverse)


list_b = [i for i in range(10)]
print(list_b)


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

output = [2*i for i in array if i != 1 and i != 9]
print(output)
