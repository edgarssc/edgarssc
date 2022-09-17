#####################--Cores--#############################################################

from distutils import core


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

def desc10(a):
    valor = a - (a * 0.1)
    return valor

def desc5(a):
    valor = a - (a * 0.05)
    return valor

def parcela2x(a):
    valor = a / 2
    return valor

def juros20(a):
    valor = a * 1.2
    return valor

#############--Código Principal--#############################################################

titulo('LOJAS GUANABARA')
preco = float(input('Digite o preço das compras: R$'))
print()
print('FORMAS DE PAGAMNTO:')
print('[ 1 ] à vista dinheiro/cheque:')
print('[ 2 ] à vista cartão:')
print('[ 3 ] 2x no cartão:')
print('[ 4 ] 3x no cartão:')
print()
opcao = int(input('Escolha sua opção: 1, 2,3 ou 4: '))
opcao1 = desc10(preco)
opcao2 = desc5(preco)
opcao3 = parcela2x(preco)
opcao4 = juros20(preco)

if opcao == 1:
    print(f'O valor da compra foi de R$ {preco:.2f}, com 10% de desconto ficou em R$ {opcao1}')
elif opcao == 2:
    print(f'O valor da compra foi de R$ {preco:.2f}, com 05% de desconto ficou em R$ {opcao2}')
elif opcao == 3:
    print(f'O valor da compra foi de R$ {preco:.2f}, parcelado em 2x de R$ {opcao3}')
else:
    print(f'O valor da compra foi de R$ {preco:.2f}, com 20% de juros, ficou em {opcao4}')    