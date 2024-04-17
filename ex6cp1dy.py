#With a nested list comprehension, find all of the numbers from [1-585] that are divisible by any single digit within [2-9].

divisiveis = [i for i in range(1, 586) if any(i % n == 0 for n in range(2, 10))] #procura números divisíveis por 2 a 9
print(divisiveis)