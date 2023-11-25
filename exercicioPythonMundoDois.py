#DESAFIO036 - FINANCIAMNETO PERGUNTE VALOR DA CASA, SALÁRIO E QUANTOS ANOS PRETENDE PAGAR.
#SE VALOR DA PARCELA MENSAL FOR SUPERIOR A 30% DO SALÁRIO NEGAR FINANCIAMENTO

print('SIMULADO FINANCIAMENTO DE IMÓVEL')

precoImovel = float(input('Preço do Imóvel: '))
rendaMensal = float(input('Rensa Mensal Atual: '))
anos = int(input('Em quantos anos pretende pagar: '))

meses = anos * 12
valorParcela = precoImovel / meses
rendaMinima = rendaMensal * 0.3

if valorParcela > rendaMinima :
    print('Emprestimo NEGADO')
else:
    print('Emprestimo APROVADO')
    print('Preço do Imóvel: R$ {:.2f} REIAS'.format(precoImovel))
    print('PAGAMENTO: {} vezes de R$ {:.2f} REAIS'.format(meses, valorParcela))




#DESAFIO037 - LEIA UM NÚMERO INTEIRO E CONVERTA EM BINÁRIO, OCTAL OU HEXADECIMAAL

#DESAFIO038 - LEIA DOIS NÚMEROS INTEIROS, COMPAREOS MOSTRANDO QUAL É O MAIOR, MENOR OU SE SÃO IGUAIS
n1 = float(input('Valor de A: '))
n2 = float(input('Valor de B: '))

 if n1 > n2:
    print(' "A" é maior que "B" ')
 elif n2 > n1: 
    print('"B" é maior que "A"')
elif n1 == n2:
    print('Os valores são IGUAIS')
print('FIM..')


#DESAFIO039 - ALISTAMENTO MILITAR
print('-----ALISTAMENTO MILITAR------')

idade = int(input('Informe sua idade: '))

if idade < 18:
    print('Você tem {} anos, ainda não está na idade de alistamento'.format(idade))
elif idade == 18:
    print('Você tem {} anos, deve se alistar imediatamente'.format(idade))
else:
    print('Você tem {} anos, está ATRASADO com o serviço militar'.format(idade))


#DESAFIO040 - NOTAS : <5 REPROVADO / =5 < 6.9 RECUPERAÇÃO / =>7 APROVADO
print('-----MÉDIA SEMESTRAL PORTUGUÊS---------')

primeiroBimestre =  float(input('Nota do Primeiro Bimestre: '))
segundoBimestre =   float(input('Nota do Segundo Bimestre: '))
terceiroBimestre =  float(input('Nota do Terceiro Bimestre: '))

mediaSemestral = (primeiroBimestre + segundoBimestre + terceiroBimestre ) / 3

if mediaSemestral < 5:
    print('Média Semestral : {}'.format(mediaSemestral))
    print('REPROVADO!!')
elif mediaSemestral == 5 or mediaSemestral < 6.9:
    print('Média Semestral : {}'.format(mediaSemestral))
    print('RECUPERAÇÃO!!')
else:
    print('Média Semestral : {}'.format(mediaSemestral))
    print('APROVADO!!')


#DESAFIO041 - RANKING ATLETAS : ATÉ 9 MIRIM / ATÉ 14 INFANTIL / ATÉ 19 JUNIOR / ATÉ 34 SENIOR / ACIMA MASTER
print('-----RANKING ATLETAS---------')

idadeAtleta = int(input('Informe idade: '))

mirim = idadeAtleta <= 9
infantil = idadeAtleta > 9 and idadeAtleta <= 14
junior = idadeAtleta > 14 and idadeAtleta <= 19
senior = idadeAtleta > 19 and idadeAtleta <= 34
master = idadeAtleta > 34

if mirim == True :
    print('IDADE {}, Categoria MIRIM'.format(idadeAtleta))
elif infantil == True:
    print('IDADE {}, Categoria INFANTIL'.format(idadeAtleta))
elif junior == True:
    print('IDADE {}, Categoria JUNIOR'.format(idadeAtleta))
elif senior == True:
    print('IDADE {}, Categoria SÊNIOR'.format(idadeAtleta))
elif master == True:
    print('IDADE {}, Categoria MASTER'.format(idadeAtleta))
    
#DESAFIO042 - DEFINA SE UM TRIANGULO É: 
#EQUILATERO: TODOS OS SÃO LADOS IGUAIS 
#ISÓSCELES:  DOIS LADOS SÃO IGUAIS
#ESCALENO:   TODOS OS LADOS SÃO DIFERENTES

print('---O TRIANGULO EXISTE ? QUAL SEU TIPO ---\n')

A = int(input('Reta A: '))
B = int(input('Reta B: '))
C = int(input('Reta C: '))

triangulo =  A + B > C and A + C > B and C + B > A

equilatero =    A == B and A == C and C == B 
isosceles =     A == B or  A == C or  C == B
escaleno =      A != B or  B != C or  A != C 


if triangulo == True and equilatero == True:
    print('TRIANGULO EQUILATERO, TODOS OS SÃO LADOS IGUAIS')
elif triangulo == True and isosceles == True:
    print('TRIANGULO ISOSCELES, DOIS LADOS SÃO IGUAIS')
elif triangulo == True and escaleno == True:
    print('TRIANGULO ESCALENO, TODOS OS LADOS SÃO DIFERENTES')
else:
    print('TRIANGULO NÃO EXISTE')
    
#DESAFIO043 - IMC - ABAIXO DE 18.5KG ABAICO DO PESO / ENTRE 18.5 E 25 IDEAL/25 A 30 SOBREPESO/ 
#30 A 40 OBESIDADE / ACIMA 40 OBESIDADE MORBIDA 
#imc = peso * altura²

import math

print('---CALCULE SEU IMC ---\n')

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

IMC = peso * (math.pow(altura,2))

if IMC < 18.5:
    print('Seu IMC é de {:.2f}'.format(IMC))
    print('ABAIXO DO IDEAL')
elif IMC == 18.5 or IMC < 25:
    print('Seu IMC é de {:.2f}'.format(IMC))
    print('IDEAL')
elif IMC == 25 or IMC < 30:
    print('Seu IMC é de {:.2f}'.format(IMC))
    print('SOBRESO')
elif IMC == 30 or  IMC < 40:
    print('Seu IMC é de {:.2f}'.format(IMC))
    print('OBESIDADE')
else: 
    print('Seu IMC é de {:.2f}'.format(IMC))
    print('OBESIDADE MÓRBIDA')

#DESAFIO044 PREÇO X CONDIÇÃO PAGAMENTO - A VISTA DINHEIRO 10% DESCONTO/ CARTÃO A VISTA 5% DESCONTO / 
#2X CARTÃO PREÇO NORMAL / 3X OU MAIS 20% JUROS 
print('---SIMULAÇÃO PAGAMENTO ---\n')
precoNormal = float(input('Informe o preço do produto:  '))
pagamento = int(input('''Digite [1] : PAGAMENTO DINHEIRO/PIX
Digite [2] : CRÉDITO/DÉB 1X
Digite [3] : CRÉDITO ATÉ 2x
Digite [4] : CRÉDITO 3X ou mais\n...  '''  ))

if pagamento == 1: 
    desconto = precoNormal*0.10
    precoFinal = precoNormal - desconto
    print('Preço Inicial: R$ {:.2f}'.format(precoNormal))
    print('Desconto: R$ {:.2f}'.format(desconto))
    print('Preço Final: R$ {:.2f}'.format(precoFinal))
elif pagamento == 2:
    desconto = precoNormal*0.05
    precoFinal = precoNormal - desconto
    print('Preço Inicial: R$ {:.2f}'.format(precoNormal))
    print('Desconto: R$ {:.2f}'.format(desconto))
    print('Preço Final: R$ {:.2f}'.format(precoFinal))
elif pagamento == 3:
    desconto = 0
    precoFinal = precoNormal 
    numeroParcelas = 2
    parcelamento = precoFinal/numeroParcelas
    print('Preço Inicial: R$ {:.2f}'.format(precoNormal))
    print('Desconto: R$ {:.2f}'.format(desconto))
    print('Preço Final: R$ {:.2f}'.format(precoFinal))
    print('Pagamento em {} parcelas, de R$ {} REAIS'.format(numeroParcelas, parcelamento))
elif pagamento == 4: 
    acrescimo = precoNormal * 0.2
    precoFinal = precoNormal + acrescimo
#INFORME DO NÚMERO DE PARCELAS
    numeroParcelas = int(input('Informe o número de parcelas... '))
    print('Preço Inicial: R$ {:.2f}'.format(precoNormal))
    print('Acréscimo: R$ {:.2f}'.format(acrescimo))
    print('Preço Final: R$ {:.2f}'.format(precoFinal))
    parcelamento = precoFinal / numeroParcelas
    print('Pagamento em {} parcelas, de R$ {} REAIS'.format(numeroParcelas, parcelamento))
else: 
     print('Opção INVÁLIDA')
    
    
       
#JOKENPPO

import random
from time import sleep

computador = random.randint (1,2)

jogador = int(input(''' 
[1] PEDRA
[2] PAPEL
[3] TESOURA
QUAL SUA JOGADA ?
'''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

print('-=' *11)
if computador == 1:
    if jogador == 1:
        print('EMPATE')
        print('Computador jogou PEDRA !!')
    elif jogador == 2:
        print('Você VENCEU !!')
        print('Computador jogou PEDRA !!')
    elif jogador ==3:
        print('Você PERDEU !!')
        print('Computador jogou PEDRA !!')
    else:
        print('Opção INVÁLIDA !!')
elif computador == 2 :
    if jogador == 1:
        print('Você PERDEU !!')
        print('Computador jogou PAPEL !!')
    elif jogador == 2:
        print('EMPATE')
        print('Computador jogou PAPEL !!')
    elif jogador ==3:
        print('Você VENCEU !!')
        print('Computador jogou PAPEL !!')
    else:
        print('Opção INVÁLIDA !!')
elif computador == 3 : 
    if jogador == 1:
        print('Você VENCEU !!')
        print('Computador jogou TESOURA !!')
    elif jogador == 2:
        print('Você PERDEU !!')
        print('Computador jogou TESOURA !!')
    elif jogador ==3:
        print('EMPATE')
        print('Computador jogou TESOURA !!')
    else:
        print('Opção INVÁLIDA !!')
   
            