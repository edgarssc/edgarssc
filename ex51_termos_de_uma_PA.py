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

#Função para título
def titulo(x):
    tam = len(x) #retorna o tamanho da string
    print('='*tam,'\n', x,'\n','='*tam)
#Função para subtítulo    
def subTitulo(X):
    tam = len(X) #retorna o tamanho da string
    print('\n','-'*tam,'\n', X, '\n', '-'*tam)

#Função que calcula os valores de uma PA e retorna a lista de valores
def calculaPA(razao,primeiroTermo):
    PA = [primeiroTermo]
    for i in range(0,9):
        proximoTermo = PA[i]+razao
        PA.append(proximoTermo)
    return PA

#############--Código Principal--#############################################################

titulo('Mostra os 10 primeiros termos de uma PA.')
razao = int(input('Digite a razão: '))
primeiroTermo = int(input('Digite o 1º termo da PA: '))
subTitulo(f'Os valores da PA são: {calculaPA(razao,primeiroTermo)}')
