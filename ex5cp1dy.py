#Compare the time to run between a loop-for and list comprehension, considering the statement: "Find the common numbers in two lists (without using a tuple or set) list_W = [1,3,7,11,22,34,57,43,89,92,93,891] list_Z = [89,1, 2, 3, 4, 5,11,22,23,34,56,891,92,43]"

from timeit import default_timer as timer

list_W = [1,3,7,11,22,34,57,43,89,92,93,891] 
list_Z = [89,1, 2, 3, 4, 5,11,22,23,34,56,891,92,43]

start = timer()
num_comum = [i for i in list_W if i in list_Z] #filtra os números da lista W que são iguais os da lista Z
stop = timer()
print(f'{stop-start:.5f} segundos')

start = timer()
num_comum = []
for i in list_W: #para o número na lista W
    if i in list_Z: #caso o mesmo número esteja na lista Z
        num_comum.append(i) #adiciona o número em comum na lista num_comum
stop = timer()
print(f'{stop-start:.5f} segundos')