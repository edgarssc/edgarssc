#####################--imports--#############################################################

from sys import stdout

#####################--Cores--#############################################################
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

titulo('Analisando números pares e impares!')
n = int(input('Digite o último número par que deverá ser exibido: '))
for i in range(1,n):
    if i % 2 == 0:
        # o end=" " e sep=' ' para evitar a quebra de linha, pois o print por padrão pulo uma linha no final e escolher o separador
        print(i,end=" ")
        #também pode usar o sys.stdout.write que não pula linha no final, porém o argumento deve ser uma string
        #stdout.write(str(i))
print(' ')

#Solução com uma quantidade menor de repetições, pois não analisa os números impares
titulo('Analisando apenas números pares!')
n = int(input('Digite o último número par que deverá ser exibido: '))
for i in range(2,n, 2):
    # o end=" " e sep=' ' para evitar a quebra de linha, pois o print por padrão pulo uma linha no final e escolher o separador
    print(i,end=" ")
    #também pode usar o sys.stdout.write que não pula linha no final, porém o argumento deve ser uma string
    #stdout.write(str(i))
print(' ')