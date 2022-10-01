#####################--imports--#############################################################


#####################--Cores--#############################################################

from sqlalchemy import false, true


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

#Função para título
def titulo(x):
    tam = len(x) #retorna o tamanho da string
    print('='*tam,'\n', x,'\n','='*tam)
#Função para subtítulo    
def subTitulo(X):
    tam = len(X) #retorna o tamanho da string
    print('\n','-'*tam,'\n', X, '\n', '-'*tam)

#############--Código Principal--#############################################################

titulo('Informa se o número é primo: ')
num = int(input('Digite um número: ').strip())
div = 0
for i in range(1,num + 1):
    if num% i == 0:
        print(cores['azul'],f'{i}',cores['limpa'],end=' ')
        div += 1
    else:
        print(cores['verde'],f'{i}',cores['limpa'],end=' ')
print()
if (div > 2):
    subTitulo(f'O numero {num} não é primo, foi divisível {div} vezes')
else:
    subTitulo(f'O numero {num} é primo, foi divisível {div} vezes')