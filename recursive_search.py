import numpy as np

lista = 1, 2, 3, 4, 5, 6, 7
target = 5

def busca_recursiva(lista, target):
    aleatorio = np.random.randint(0, len(lista))
    print('indice aleatorio é:', aleatorio)
    print('#----------------TENTATIVAS-----------------#')
    if target == lista[aleatorio]:
        print('#-----------------ACABOU--------------------#')
        return lista.index(lista[aleatorio])
    if target > lista[aleatorio]:
        print('Target era maior. roda dnv!')
        lista = lista[aleatorio:]
        print('lista nova agora é,', lista)
        return busca_recursiva(lista, target)
    if target < lista[aleatorio]:
        print('Target era menor. Roda dnv!')
        lista = lista[:aleatorio]
        print('nova lista agora é:',lista)
        return busca_recursiva(lista, target)

busca_recursiva(lista, target)
