#####################--imports--#############################################################


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

titulo('Soma de todos os números impares que são multiplos de 3 e que se encontram no intervalo de 1 até 500.')
print()
soma = 0
qtd = 0
#busca apenas numeros impares indo a partir do 1 de 2 em dois
for i in range(1,501,2):
    if i % 3 == 0:
        print(i, end=' ')
        soma += i
        qtd += 1 
print()
print(f'A soma de todos os números impares multiplos de 3 é: {cores["azul"]}{soma}{cores["limpa"]} o total de números utilizados na soma foi de {cores["verde"]}{qtd}{cores["limpa"]}')