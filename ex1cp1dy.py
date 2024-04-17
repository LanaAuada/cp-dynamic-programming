#Make a function to produce a new list, derived from an initial one, by adding 3 to all odd numbers inside this initial list. Use list comprehension.

def Adiciona(ListaInicial): #define a função que adicionará três a cada número ímpar da lista
    return [i + 3 if i % 2 != 0 else i for i in ListaInicial]

ListaInicial = [1, 2, 3, 4, 5, 6, 7, 8]

NovaLista = Adiciona(ListaInicial) #armazena o resultado retornado pela função em uma nova variável
print(NovaLista)
