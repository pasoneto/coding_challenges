#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string
import numpy as np
#Função contagem
def contagem(caso, alfabeto):
    alfabeto = alfabeto
    contagem = []
    for k in alfabeto:
        for i in caso:
            oi = i.count(k)
            contagem.append(oi)
    return contagem


# In[6]:


#Função para somar os resultados de ambos os casos
def somando(caso):
    fim = []
    cont_maiusculo = contagem([caso], string.ascii_lowercase) 
    #print(cont_maiusculo)
    cont_minusculo = contagem([caso], string.ascii_uppercase)
    #print(cont_minusculo)
    for i in range(len(cont_maiusculo)):
        fim.append(cont_maiusculo[i] + cont_minusculo[i])
    return fim

#Chamando a função
#somando('aaAAIUHAIEUHiushiuhsiuhISURHISUHIUiusrhiurshiuHIURHSIURHIhisurhiuh')


# In[54]:


#Calculando porcentagens. Função retorna todas as porcentagens de cada letra.
def fcont(caso):
    result = somando(caso)
    porcentagens = []
    for i in result:
        porcentagens.append(i/sum(result)*100)
    return(porcentagens)

def ondeta(caso):
    oi = fcont(caso)
    alfabeto  = string.ascii_lowercase
    maior = 0
    for i in oi:
        if i > maior:
            maior = i
    print(maior)
    indices = [k for k, n in enumerate(oi) if n == maior]
    print(indices)
    letras = []
    for j in indices:
        letras.append(alfabeto[j])
    return (letras, max(oi))


ondeta('asl;dzc]ewa;d]sd.vcxhkjasdfa]]bkjolnnopuibuiopjl;')


# In[62]:


penis = 1, 4, 5, 2, 5, 6
lista = []
for i in penis:
    lista.append(i)
lista
    


# In[ ]:





# In[ ]:





# In[ ]:




