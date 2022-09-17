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
    
#############--Código Principal--#############################################################

perfumaria('Analisador de Triângulos')

s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))

#regra do triângulo: cada um dos lados deve ser menor que a soma dos outros dois
if (s1 < (s2 + s3)) and (s2 < (s1 + s3)) and (s3 < (s1 + s2)):
    print()
    print('É possível formar um triângulo:')
    if (s1 == s2) and (s1 == s3):
        print()
        perfumaria(f'Triangulo {cores["azul"]}EQUILATERO{cores["limpa"]}, todos os lados são iguais!')

    elif (s1 == s2) or (s1 == s3) or (s2 == s3):
        print()
        perfumaria(f'Triangulo {cores["azul"]}ISÓSCELES{cores["limpa"]}, dois lados são iguais!')
    else:
        print()
        perfumaria(f'Triangulo {cores["azul"]}ESCALENO{cores["limpa"]}, todos os lados são diferentes!')
else:
    print('não é possível formar um triângulo:')

