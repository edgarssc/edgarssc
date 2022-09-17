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

def calcImc(a,b):
    imc = a / (b**2)
    return imc


#############--Código Principal--#############################################################

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = calcImc(peso,altura)
if imc <= 18.5:
    perfumaria(f'Para uma pessoa com {cores["roxo"]}{peso}Kg{cores["limpa"]} e {cores["roxo"]}{altura}m{cores["limpa"]} seu IMC é de {cores["vermelho"]}{imc:.2f}, Abaixo do peso{cores["limpa"]}.')
elif (imc > 18.5) and (imc <= 25):
    perfumaria(f'Para uma pessoa com {cores["roxo"]}{peso}Kg{cores["limpa"]} e {cores["roxo"]}{altura}m{cores["limpa"]} seu IMC é de {cores["verde"]}{imc:.2f}, Peso ideal{cores["limpa"]}.')
elif (imc > 25) and (imc <= 30):
    perfumaria(f'Para uma pessoa com {cores["roxo"]}{peso}Kg{cores["limpa"]} e {cores["roxo"]}{altura}m{cores["limpa"]} seu IMC é de {cores["amarelo"]}{imc:.2f}, Sobrepeso{cores["limpa"]}.')    
else:
    perfumaria(f'Para uma pessoa com {cores["roxo"]}{peso}Kg{cores["limpa"]} e {cores["roxo"]}{altura}m{cores["limpa"]} seu IMC é de {cores["vermelho"]}{imc:.2f}, Obesidade Morbida{cores["limpa"]}.')    