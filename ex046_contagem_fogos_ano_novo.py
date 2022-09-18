#####################--Cores--#############################################################

from random import randint
from time import sleep


cores = {'limpa':'\033[m',
         'azul':'\033[1;34m',
         'amarelo':'\033[1;33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'roxo':'\033[1;35m'}

cores_fundo = {'limpa':'\033[m',
         'azul':'\033[1;44m',
         'amarelo':'\033[1;43m',
         'pretoebranco':'\033[7;40m',
         'vermelho':'\033[1;41m',
         'verde':'\033[1;42m',
         'roxo':'\033[1;45m'}

#############--Funções--#####################################################################

def perfumaria(X):
    print('-='*40)
    print(X)
    print('-='*40)

def titulo(x):
    print()
    print('='*10, x, '='*10)
    print()

#############--Código Principal--#############################################################

perfumaria('Contagem regressiva para o Ano Novo!!!!!')
for i in range(10,-1,-1):
    print(i)
    sleep(1)
print('FELIZ ANO NOVO!!!!!')
