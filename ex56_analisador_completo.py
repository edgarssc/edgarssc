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
def maiorPeso(lista):
    maior = max(lista)
    return maior

#Função para saber o menor peso
def menorPeso(lista):
    menor = min(lista)
    return menor

#############--Código Principal--#############################################################
lista_pesos = [] #lista para guardar os pesos
qtd_pessoas = int(input('Digite a quantidade de pessoas: '))
somaidade = 0
maioridadehomem = 0
nomehomemaisvelho = ""
totalmulheresmenorde20 = 0
for i in range(1,qtd_pessoas + 1):
    print(f'--------- {i}ª PESSOA ---------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    somaidade += idade
    if i == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomehomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomehomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulheresmenorde20 += 1

mediaidade = somaidade / qtd_pessoas
print(f'A média de idade é de {mediaidade:.2f}.')
print(f'O home mais velho tem {maioridadehomem} anos e se chama {nomehomemaisvelho} .')
print(f'São {totalmulheresmenorde20} mulheres com menos de 20 anos.')