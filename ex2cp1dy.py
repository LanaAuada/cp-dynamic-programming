#Apply the above function to the following initial lists: a = [2,3,5,6,7,8,11,13,14,15,17,18,19,20,2003,31,32,45,47] b = [3,4,5,7,99,8,24,32,33,35,37,23,73,77,81,83,85,89,93,96,99] Compute the time to run the function for the two cases.

from timeit import default_timer as timer

def Adiciona(ListaInicial): #define a função que adicionará três a cada número ímpar da lista
    return [i + 3 if i % 2 != 0 else i for i in ListaInicial]


a = [2,3,5,6,7,8,11,13,14,15,17,18,19,20,2003,31,32,45,47]
b = [3,4,5,7,99,8,24,32,33,35,37,23,73,77,81,83,85,89,93,96,99]


start = timer()
NovaLista_a = Adiciona(a) #chama a função com a lista "a" e armazena o resultado em "NovaLista_a"
print(NovaLista_a)
stop = timer()
print(f'{stop-start:.4f} segundos')

start = timer()
NovaLista_b = Adiciona(b) #chama a função com a lista "b" e armazena o resultado em "NovaLista_b"
print(NovaLista_b)
stop = timer()
print(f'{stop-start:.4f} segundos')

