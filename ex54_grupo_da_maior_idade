from datetime import datetime

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

#Função para saber se a pessoa é maior de idade
def maiorDeIdade(idades):
    now = datetime.now()
    maior_de_idade = 0
    for i in range(len(idades)):
        if (now.year - idades[i] ) >= 18:
            maior_de_idade += 1
    return maior_de_idade

#Função para saber se a pessoa é menor de idade
def menorDeIdade(idades):
    now = datetime.now()
    menor_de_idade = 0
    for i in range(len(idades)):
        if (now.year - idades[i]) < 18:
            menor_de_idade += 1
    return menor_de_idade

#############--Código Principal--#############################################################
idades = [] #lista para guardar as idades
qdt_pessoas = 8 #armazena a quantidade de pessoas analisadas
for i in range(1,qdt_pessoas):
    idades += [int(input(f'Em que ano a {i}º pessoa nasceu? '))]
print (f'Ao todo tivemos {maiorDeIdade(idades)} pessoas maiores de idade e também {menorDeIdade(idades)} menores de idade.')



