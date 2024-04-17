#Develop a code to find all of the numbers from 1-857 that are divisible by 7 and 3. You may use a 'loop-for' or 'list comprehension'.

a = [i for i in range(1,858) if i % 7 == 0 and i % 3 == 0] #número em uma faixa de 1 a 857, acha os números nessa faixa que são divisíveis por 7 e por 3, armazena esses números em uma lista
print(a)
