#Explain the meaning of the following function: (Answer in Portuguese or English) def menu_wow(meals): for i in range(len(meals)-1): if meals[i] == meals[i+1]: return True return False

def menu_wow(meals): #define a função
  for i in range(len(meals)-1): #percorre até o penúltimo elemento
    if meals[i] == meals[i+1]: #verifica se o próximo elemento da lista é igual ao atual
       return True
  return False

#Assim, essa função serve para verificar se existem itens iguais consecutivos no menu, retornando False caso não haja e True casa haja dois itens consecutivos iguais.