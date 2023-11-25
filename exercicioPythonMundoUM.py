#DESAFIO028 - Jogo adivinhação de número
import random
x = random.randint(0,6)

numero = int(input('Diga um número de 0 a 6...'))

if numero == x :
    print('PARABÉNS VOCÊ ACERTOU ! O NÚMERO MISTERIOSO É {}'.format(x))
else:
    print('ERROU! O NÚMERO MISTERIOSO É {}, VOCÊ CHUTOU {}'.format(x,numero))
___________________________________________________________________________________
#DESAFIO029 - LEIA A VELOCIDADE DE UM CARRO. SE ULTRAPASSAR 80KM/H MULTA. CALCULE MULTA: 7 REAIS PRA CADA KM ACIMA DO LIMITE

velocidade = float(90)
multa = (velocidade - 80) * 7

if velocidade <= 80:
    print('LIMITE PERMITIDO')
else:
    print('ACIMA DO LIMITE PERMITIDO')
    print('MULTA DE R$ {:.2f} REIAS'.format(multa))
_______________________________________________________________________________________    
#DESAFIO030 LEIA UM NÚMERO INT E MOSTRE SE É PAR OU IMPAR

n = int(input('Digite um número'))

if (n % 2) == 0 :
    print('NÚMERO PAR')
else:
    print('NÚMERO ÍMPAR')
_______________________________________________________________________________________
#DESAFIO31 PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM. SE FOR ATÉ 200KM 0.50 CENTAVOS POR KM. VIAGENS MAIS LONGAS 0.45 POR KM   

distancia = float(input('Informe a distância até o destino...'))

if distancia <= 200 :
    taxaPorKm = 0.50
    taxaTotal = distancia * taxaPorKm
    print('Preço final R$ {} REAIS'.format(taxaTotal))
else :
    taxaPorKm = 0.45
    taxaTotal = distancia * taxaPorKm
    print('Preço final R$ {} REAIS'.format(taxaTotal))
print('\n--BOA VIAGEM--')
_______________________________________________________________________________________
#DESAFIO33 LEIA 3 NÚMEROS, E INFORME QUAL O MAIOR E QUAL O MENOR
primeiro = int(input('Primeiro número....'))
segundo = int(input('Segundo número....'))
terceiro = int(input('Terceiro número....'))

maior = primeiro
menor = primeiro

if segundo > maior:
    maior = segundo

if terceiro > maior:
    maior = terceiro
    
if segundo < menor:
    menor = segundo

if terceiro < menor:
    menor = terceiro    

print('MAIOR NÚMERO É {}'.format(maior))
print('MENOR NÚMERO É {}'.format(menor))
_______________________________________________________________________________________
#DESAFIO34 AUMENTO SALARIAL SALARIOS SUPERIORES A 1250,00 10% AUMENTO --- INFERIORES OU IGUAIS 15%
 
salario = float(input('Informe seu salário pra cálculo de reajuste: '))

ajuste1 = 0.1
ajuste2 = 0.15

if salario > 1250.0 :
    salarioAtual = salario + (salario * ajuste1)
    print('Você teve um ajuste de {}%, portanto seu salário atual será de: R$ {} REAIS '.format(ajuste1*100, salarioAtual))
else:
    salarioAtual = salario + (salario * ajuste2)
    print('Você teve um ajuste de {}%, portanto seu salário atual será de: R$ {} REAIS '.format(ajuste2*100, salarioAtual))


#DESAFIO35 LEIA O CUMPRIMENTO DE 3 RETAS E INFORME SE ELAS FORMAM UM TRIÂNGULO

print('TESTE SE O TRIÂNGULO É VERDADEIRO')
a = float(input('Informe o comprimento da reta A..'))
b = float(input('Informe o comprimento da reta B..'))
c = float(input('Informe o comprimento da reta C..'))

if a + b > c and a + c > b and b + c > a :
    print('HÁ UM TRIÃNGULO')
else :
    print('NÃO HÁ TRIÃNGULO')