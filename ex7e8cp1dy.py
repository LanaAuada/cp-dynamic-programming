#Define a function to compute 3 things: the quantity of numbers within a list, a list with the numbers from the list divisible by 3 or 5, and indicate the quantity of numbers not following this criteria. You may use list comprehension or loop-for.

def analisa(Lista):

    quantidade = len(Lista) #calcula a quantidade de elementos na lista

    divisiveis_3_5 = [i for i in Lista if i % 3 == 0 or i % 5 == 0] #cria uma lista que contém os números da outra lista que são divisíveis por 3 ou 5

    quantidade_nao_divisivel = quantidade - len(divisiveis_3_5) #subtrai a quantidade de números divisíveis por 3 ou 5 da quantidade total de elementos da lista para achar a quantidade de elementos não divisíveis por 3 ou 5

    return quantidade, divisiveis_3_5, quantidade_nao_divisivel

#Using the functions derived in the last question (#_7), show the result upon: a5 = [3,5,6,12,13,18,20,22,24,40,41,17,21,1004,49,51,44,63,66,79] b5 = [1,2,4,6,9,10,11,45,32,33,1308,88,67,47,56,89,95,92,100,16,15] c5 = [3,4,5,6,9,10,44,34,33,37,41,42,50,52,1404,53,67,58,68,72,74,75]

a5 = [3,5,6,12,13,18,20,22,24,40,41,17,21,1004,49,51,44,63,66,79]
b5 = [1,2,4,6,9,10,11,45,32,33,1308,88,67,47,56,89,95,92,100,16,15]
c5 = [3,4,5,6,9,10,44,34,33,37,41,42,50,52,1404,53,67,58,68,72,74,75]

a5resul = analisa(a5)
print(a5resul)

b5resul = analisa(b5)
print(b5resul)

c5resul = analisa(c5)
print(c5resul)