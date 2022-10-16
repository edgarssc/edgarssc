from csv import list_dialects


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

#Função para saber se o maior peso
def maiorPeso(lista_pesos):
    maior_peso = max(lista_pesos)
    return maior_peso

#Função para saber o menor peso
def menorPeso(lista_pesos):
    maior_peso = min(lista_pesos)
    return maior_peso

#############--Código Principal--#############################################################
lista_pesos = [] #lista para guardar os pesos
for i in range(1,6):
    lista_pesos += [float(input(f'Peso da {i}º pessoa: '))]
print (f'O maior peso lido foi {maiorPeso(lista_pesos)}Kg e o menor peso foi {menorPeso(lista_pesos)}Kg.')