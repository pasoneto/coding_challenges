#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
import json
import numpy as np
import string as str
from datetime import datetime
from datetime import date


# In[2]:


#API key = 0bbd09d9d688940fa0354fb3a4aeffe4
#--------------------------------------------FUNÇÕES BASE--------------------------------------------------------------#

#------------------PEGANDO OS FILMES DE UM ANO X---------------------------#
def lista_filmes(ano):
    return requests.get(f'https://api.themoviedb.org/3/discover/movie?api_key=0bbd09d9d688940fa0354fb3a4aeffe4&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=10&primary_release_year={ano}')
#Esta função terorna: lista completa com todas as informações sobre um filme. Devo parsear tudo e ficar apenas com uma lista
#de ids e datas de lançamento dos filmes.

#------------------PEGANDO AS IDADES DE UM ATOR X---------------------------#
def idade(ator):
    return requests.get(f'https://api.themoviedb.org/3/person/{ator}?api_key=0bbd09d9d688940fa0354fb3a4aeffe4&language=en-US')
#Esta função me retorna todas as informações da vida de um ator. Devo parsear até ficar só com a data de nascimento.


# In[15]:


#Parseando as informações de um filme de um determinado ano.
def filmes_df(inicio, fim):
    anos = list(range(inicio,fim+1))
    filmezins = []
    for i in range(len(anos)):
        filmes = lista_filmes(anos[i]).json()['results']
        filmes = pd.DataFrame.from_dict(filmes)
        filmes = filmes[filmes.original_language == "en"]
        filmes = filmes[['id', 'release_date']]
#         print(filmes)
        filmezins.append(filmes)
    filmezins = pd.concat(filmezins, ignore_index=True)
    return filmezins
filmes = filmes_df(2005, 2005)


# In[16]:


filmes


# In[17]:


#------------------PEGANDO TODOS ATORES DE TODOS FILMES DE UM ANO X---------------------------#
#Os anos são determinados pela lista filmes['ids'], que vêm do data frame acima.
def creditos():
    ids = list(filmes['id'])
    creditos = []
    for i in ids:
        penis = requests.get(f'https://api.themoviedb.org/3/movie/{i}/credits?api_key=0bbd09d9d688940fa0354fb3a4aeffe4')
        penis = penis.json()
        creditos.append(penis)
    creditos = pd.DataFrame(creditos)
    return creditos['cast']
#Função me retorna todas as informações sobre todos os atores de todos os filmes de um ano X. Abaixo eu parseio
#essa informação e fico apenas com os ids de cada ator, que serão utilizados depois para pegar a sua idade
#(que não consta na função 'credito()')

#------------------FUNÇÃO PARA PEGAR TODOS OS IDS DE TODOS OS ATORES DE TODOS OS FILMES DO DATA FRAME INICIAL----------------#
def todos_filmes():
    oi = creditos()
    todos = []
    for k in range(len(oi)):
        #Cada k é um filme. Eu transformo em data frame porque aí eu posso chamar o 'ID' de cada ator, em cada filme. 
        #Daí já transformo pra lista imediatamente:
        penis = list(pd.DataFrame(oi[k])['id'])
        todos.append(penis)
    return todos
#Função retorna uma lista com listas dentro. Cada sub lista contem todos os ids de todos os 
#atores de cada filme do ano X

#Reunindo ao data frame principal:
filmes['atores'] = todos_filmes()


# In[18]:


filmes


# In[26]:


#-------------------FUNÇÃO PARA PEGAR TODAS AS INFORMAÇÕES DE UM DETERMINADO ATOR----------------------#
def idade(ator):
    return requests.get(f'https://api.themoviedb.org/3/person/{ator}?api_key=0bbd09d9d688940fa0354fb3a4aeffe4&language=en-US')

#---------------------FUNÇÃO PARA EXTRAIR APENAS A DATA DE NASCIMENTO DE CADA ATOR E ORGANIZAR OUTPUT POR FILME--------------# 
def idades_dos_atores():
    #Para percorrer o data frame inicial, eu transformo as informações em lista:
    oi = list(filmes['atores'])
    #Para separar grupos de atores de acordo com filme, eu criei essa lista com listas vazias, que eu uso para 
    #apendar separadamente as infos de cada filme.
    final = [[] for i in range(len(oi))]
    for k in range(len(oi)):
        for i in range(len(oi[k])):
            penis = idade(oi[k][i]).json()
            penis = penis['birthday']
            if penis != None:
                #Aqui eu apendo cada filme para o seu respectivo [] na lista final.
                final[k].append(penis)
    return final
filmes['ano_atores'] = idades_dos_atores()


# In[27]:


#--------------------FAZENDO ALGUNS AJUSTES AO BANCO DE DADOS-----------------------#

#Problema da data: As datas vieram como string e eu preciso transformá-las em objeto de data:
oi = list(filmes['ano_atores'])
#Transformando de string para date object
for k in range(len(oi)):
    for i in range(len(oi[k])):
        oi[k][i] = datetime.strptime(oi[k][i], '%Y-%m-%d').date()

filmes['ano_atores'] = oi
#Transformando release dates em date objects também
karai_biridin = list(filmes['release_date'])
for i in range(len(karai_biridin)):
    karai_biridin[i] = datetime.strptime(karai_biridin[i], '%Y-%m-%d').date()

#Juntando o resultado ao data frame principal:
filmes['release_date'] = karai_biridin


# filmes

# In[29]:


#Calculando idade final
#Preciso dar um jeito de subtrair a idade de release pela idade do ator.
# Algo deste tipo:

oi = list(filmes['ano_atores'])
oi2 = list(filmes['release_date'])
final = [[] for i in range(len(oi))]
for k in range(len(oi)):
    for i in range(len(oi[k])):
        final[k].append(oi2[k].year - oi[k][i].year)

#Reunindo no banco de dados:
filmes['idades'] = final


# In[31]:


#------------------------------CÁLCULOS FINAIS-----------------------------#
#Função para separar data frame por anos.
def separando_por_ano(ano):
    date_from = pd.Timestamp(date(ano,1,1))
    date_to = pd.Timestamp(date(ano,12,31))
    penis = filmes[(filmes['release_date'] > date_from ) & (filmes['release_date'] < date_to)]
    return penis

#Função para calcular media de idade por ano.
def media_por_ano(ano):
    karai_darti = list(separando_por_ano(ano)['idades'])
    geral = []
    for i in range(len(karai_darti)):
        oi = np.mean(karai_darti[i])
        geral.append(oi)
    return np.nanmean(geral)

#Função para retornar uma lista com todas as médias de anos.
def lista_medias(inicio, fim):
    anos = list(range(inicio, fim+1))
    final = []
    for i in range(len(anos)):
        media = media_por_ano(anos[i])
        final.append(media)
    return final
lista_medias(2005, 2005)


# In[ ]:





# In[ ]:




