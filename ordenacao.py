import numpy as np
a = [1, 6, 4, 8, 4, 2, 5, 7, 8, 4, 23, 6, 5, 43, 23, 75, 79, 56]
def menor(lista):
    ordenado = []
    oi = a[0]
    for i in lista:
        if i < oi:
            oi = i
    return oi
menor(a)

def ord(lista):
    ordenado = []
    lista = lista
    for i in range(len(lista)):
        oi = menor(lista)    
        ordenado.append(oi)
        lista.remove(oi)
    print(ordenado)
