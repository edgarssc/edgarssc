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


def titulo(x):
    tam = len(x) #retorna o tamanho da string
    print('\n','='*tam,'\n', x, '\n', '='*tam)
    
def subTitulo(X):
    tam = len(X) #retorna o tamanho da string
    print('\n','-'*tam,'\n', X, '\n', '-'*tam)

#############--Código Principal--#############################################################

num = int(input('Digite um número para ver sua tabuada: '))
for i in range(1,10):
    print(f'{i} x {num} =', i * num,)