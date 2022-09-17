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
print()
print('''Suas opções:\n

[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
print()

lista = ['PEDRA', 'PAPEL', 'TESOURA']

#variável para guardar a escolha do jogador
opcao = int(input('Digite sua jogada? '))

#variável para guardar a escolha do computador por meio de um retorno de um valor inteiro dentre 0 e 2
pcjoga = randint(0,2) 

#função python para aguardar uma quantidade de segundos passada por parametro
sleep(1)
print(f'{cores["amarelo"]}JO{cores["limpa"]}')
sleep(1)
print(f'{cores["azul"]}KEN{cores["limpa"]}')
sleep(1)
print(f'{cores["roxo"]}PO!!!{cores["limpa"]}')
print()
perfumaria(f'''O computador jogou {cores["roxo"]}{lista[pcjoga]}{cores["limpa"]} e você jogou {cores["roxo"]}{lista[opcao]} {cores["limpa"]}''')
print()

# caso o computador escolha 0
if pcjoga == 0 and opcao == 0:
    titulo(f'{cores["amarelo"]}EMPATOU{cores["limpa"]}')
elif pcjoga == 0 and opcao == 1:
    titulo(f'{cores["verde"]}VOCÊ GANHOU!!!!{cores["limpa"]}')
elif pcjoga == 0 and opcao == 2:
    titulo(f'{cores["vermelho"]}VOCÊ PERDEU!!!!{cores["limpa"]}')

# caso o computador escolha 1
if pcjoga == 1 and opcao == 1:
    titulo(f'{cores["amarelo"]}EMPATOU{cores["limpa"]}')
elif pcjoga == 1 and opcao == 2:
    titulo(f'{cores["verde"]}VOCÊ GANHOU!!!!{cores["limpa"]}')
elif pcjoga == 1 and opcao == 0:
    titulo(f'{cores["vermelho"]}VOCÊ PERDEU!!!!{cores["limpa"]}')

# caso o computador escolha 2
if pcjoga == 2 and opcao == 2:
    titulo(f'{cores["amarelo"]}EMPATOU{cores["limpa"]}')
elif pcjoga == 2 and opcao == 0:
    titulo(f'{cores["verde"]}VOCÊ GANHOU!!!!{cores["limpa"]}')
elif pcjoga == 2 and opcao == 1:
    titulo(f'{cores["vermelho"]}VOCÊ PERDEU!!!!{cores["limpa"]}')