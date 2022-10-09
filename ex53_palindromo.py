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

#Função para título
def titulo(x):
    tam = len(x) #retorna o tamanho da string
    print('='*tam,'\n', x,'\n','='*tam)
#Função para subtítulo    
def subTitulo(X):
    tam = len(X) #retorna o tamanho da string
    print('\n','-'*tam,'\n', X, '\n', '-'*tam)

def inverterFrase(x):
    invertida = ''
    for i in range(len(x) -1,-1,-1):
        invertida += frase[i]
    return invertida
#############--Código Principal--#############################################################

frase = str(input('Digite uma frase: ').replace(' ','').upper())
# outra forma de fazer seria:
#   palavras = frase.split()
#   tudojunto = ''.join(palavras)


if inverterFrase(frase) == frase:
    print(f'A frase foi',cores['azul'],{frase},cores['limpa'], ' e o contrário ficou', cores['amarelo'],{inverterFrase(frase)},cores['limpa'],' e esta frase é um PALINDROMO!')
else:
    print(f'A frase foi',cores['azul'],{frase},cores['limpa'], ' e o contrário ficou', cores['amarelo'],{inverterFrase(frase)},cores['limpa'],' e esta frase não é um PALINDROMO!')