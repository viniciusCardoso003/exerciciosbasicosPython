#DESAFIO046 contagem regressiva 10 até 0. 1 segundo de pausa

from time import sleep

for c in range (10, -1, -1 ):
    print(c)
    sleep(1)
print('FOGOS !!!!')

#DESAFIO047 mostrar na tela todos os números pares que estão no intervalo de 1 e 4 

for c in range (1, 51, +2):
    if c % == 2:
        print(c)
        
        #OU, E MAIS INTELIGENTE

for c in range (2, 51, 2):
        print(c)
print('FIM')


#DESAFIO048 A SOMA ENTRE NUMEROS IMPARES QUE SÃO MÚLTIPLOS DE 3, QUE SE ENCONTRAM ENTRE 1 ATÉ 500

soma = 0
cont = 0 

for c in range (1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores solicitados é igual {} '.format(cont, soma))   

#DESAFIO049 TABUADA

print('=-'*6, 'TABUADA', '=-'*6)

n = int(input(' Digite um número pra calculo: '))
print('=-'*16)

for c in range(0,11):
    x = n * c
    print('{} x {} = {}'.format(n,c,x))
    
    #OU com for simplificado
    
for c in range(0,11):
    print('{} x {} = {}'.format(n,c, n*c))
    
#DESAFIO049 LEIA 6 NÚMERO INTEIROS,MOSTRE A SOMA DOS NÚMEROS PARES, SE IMPAR DESCONSIDERAR

soma = 0 
cont = 0
for c in range(1,6):
    n = int(input('Digite o valor {}: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} números PARES, a soma foi de {}'.format(cont, soma))

#DESAFIO050 leia 6 números e some os pares

pares = 0

for c in range (1, 7):
    n = int(input('Digite o valor {}: '.format(c)))
    if n % 2 == 0:
        pares += n
print('A soma dos pares foi: {}'.format(pares))

#DESAFIO051 10 termos de uma P.A

primeiroTermo = int(input('Informe o primeiro termo da P.A : '))
razao = int(input('Razão da P.A : '))
decimoTermo = primeiroTermo + (10 - 1)* razao

for c in range (primeiroTermo, decimoTermo + 1 , razao):
    print(c)
print('ACABOU!')

#DESAFIO054 ler o ano de nascimento de 7 pessoas. mostre quantas são maiores e quantas menores de idade

from datetime import date

atual = date.today().year
maiores = 0
menores = 0

for c in range (1, 8):
    nascimento = int(input('Informe seu ano de nascimento: '))
    if atual - nascimento <  18:
        menores += 1
    else:
        maiores +=1
print('Há {} maiores de idade'.format(maiores))
print('Há {} menores de idade'.format(menores))

#DESAFIO055: Leia o peso de cinco pessoas. MOstre o maior e o menor peso. 

maior = 0
menor = 0

for p in range (1,6):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso informado foi de {} Kg'.format(maior))
print('O menor peso informado foi de {} Kg'.format(menor))

#DESAFIO056: Leia nome, idade e sexo de 4 pessoas. Mostre: média de idade, nome do homem mais velho , quantas mulheres tem < 20 anos

somaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
mulheresMenosVinte = 0

for p in range (1,5):
    print('-----{}º PESSOA-----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo(M/F): '))
    somaIdade += idade
    
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
            maiorIdadeHomem = idade
            nomeVelho = nome
    
    if sexo in 'Ff' and idade < 20:
        mulheresMenosVinte += 1
    
print('=-'*16) 
print('A média de idade do grupo é de {:.2f} anos'.format((somaIdade / 4))) 
print('=-'*16)
print('O homem mais velho se chama {}, e tem {} anos'.format(nomeVelho, maiorIdadeHomem))
print('=-'*16)
print('{} mulher(es) tem menos de 20 anos'.format(mulheresMenosVinte))

#DESAFIO057: leia o sexo que só aceite M ou F. Caso errado peça para digitar novamente

sexo = str(input('M/F: '))

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Tente novamente usando: "M" ou "F": '))
print('Comando aceito')

#DESAFIO058 JOGO ADIVINHA NUMERO EM WHILE

from random import randint

a = randint(1,10)
print(a)
cont = 1

aposta = int(input('Qual é sua jogada ? Fale um número de 1 a 10...'))

while a != aposta:
    aposta = int(input('Você ERROU Tente outra Vez...\n----'))
    cont += 1
print('=-'*16)    
print('Você ACERTOU na {}° tentativa !!'.format(cont))

#DESAFIO059 -LEIA DOIS VALORES - MOSTRE UM MENU SOMAR / MULITPICAR M/ MAIOR / NOVOS NUMEROS / SAIR 
from time import sleep

a = int(input('Informe valor de "A":  '))
b = int(input('Informe valor de "B":  '))
print('=-='*17)
opcao = 0

while opcao != 5:
    print('''[1] SOMAR 
[2] MULTIPLICAR
[3] MAIOR
[4] DEFINIR NOVOS NÚMEROS
[5] SAIR''')
    opcao = int(input('O que deseja fazer? '))
    print('=-='*17)
    
    if opcao == 1: 
        print('A Soma entre {} e {} é igual a: {}'.format(a,b, a+b))
        print('=-='*17)
    
    elif opcao == 2:
        print('O Produto entre {} e {} é igual a: {}'.format(a,b, a*b))
        print('=-='*17)
    
    elif opcao == 3:
        if a > b:
            print('{} é maior que {}, portanto A é maior que B'.format(a,b))
            print('=-='*17)
        elif b > a:
            print('{} é maior que {}, portanto B é maior que A'.format(b,a))
            print('=-='*17)
        else:
           print('{} e {} são iguais'.format(a,b))
           print('=-='*17)
   
    elif opcao == 4:
        print('VAMOS NOVAMENTE')
        a = int(input('Informe valor de "A":  '))
        b = int(input('Informe valor de "B":  '))
        print('=-='*17)
    
    elif opcao == 5:
        print('Finalizando....')
        sleep(2)
        break
    
    else:
        print('Opção Inválida, tente novamente..')
        print('=-='*17)
       
print('=-='*17)
print('FIM')

#DESAFIO061 - leia um número qualquqer e veja fatorial

n = int(input('Valor para Calculo: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

    #Ou Usando Biblioteca

from math import factorial

n = int(input('Valor para Calculo: '))
print('Fatorial de {} é {}'.format(n,factorial(n)))

#DESAFIO061 - progressão aritmética , com 10 primeiros termos

print('Gerador de P.A')
print('=-'*10)

n = int(input('Qual o primeiro termo da P.A? '))
r = int(input('Qual a razão da P.A? '))
c = 1

while c <= 10:
    print('{}°termo: {}'.format(c, n))
    n = n + r
    c += 1
print('FIM')

#DESAFIO062 - progressão aritmética , perguntando o número de termos

print('Gerador de P.A')
print('=-'*10)

primeiro = int(input('Qual o primeiro termo da P.A? '))
r = int(input('Qual a razão da P.A? '))
termo = primeiro
c = 1
total = 0 
mais = 3

while mais != 0:
    total = total + mais
    while c <= total:
        print('{}°termo :{}'.format(c, termo))
        termo += r
        c +=1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais ?'))
print('FIM')

#DESAFIO063 - FIBONACCI

n = int(input('Deseja ver quais termos da sequência?'))
t1 = 0 
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
cont = 3

while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')

#DESAFIO064 - LEIA VÁRIOs NÚMERO. O PROG VAI PARAR QUANDO FOR DIGITADO 999. MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E A SOMA ENTRE ELES - 999

n = 0
c = 0
soma = 0
n = int(input('Qual valor? [999 para parar]:  '))

while n != 999:
    soma += n
    c+= 1
    n = int(input('Qual valor? [999 para parar]: '))
print('Você digitou {} termos e a soma foi de {}'.format(c,soma))    
print('FIM')

#DESAFIO065 - leia vários numeros. no final media entre todos, qual o maior e menor . perguntar se quer continuar .

resp = 'S'
soma = c = media = maior = menor = 0
maior = 0
menor = maior

while resp in 'Ss':
    n = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N]? '))
    print('^^'*15)
    soma = soma + n
    c += 1
    
    if c == 1:
        maior = menor = n
    else: 
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma/c    
print('Foram digitados {} números, a média entre eles é de: {:.2f}'.format(c, media))
print('O maior numero foi {}'.format(maior))
print('O menor numero foi {}'.format(menor))
print('FIM!!')

#DESAFIO066 - exercicio 64 com break

n = c = soma =  0

while True:
    n = int(input('Qual valor? [999 para parar]:  '))
    if n == 999:
        break
    else: 
        soma += n
        c+= 1
print(f'Você digitou {c} termos e a soma foi de {soma}')    
print('FIM')

#DESAFIO067 - Tabuada versão 2

print('=-'*5, 'TABUADA', '=-'*5)
while True:
    c = 0
    print('=-'*15)
    n = int(input('Digite o valor: '))
    if n < 0:
        break
    else:
        print(f'TABUADA DO {n}')
        while c <= 10 :
            x = n * c
            print(f'{n} x {c} = {x}')
            c += 1
print('FIM')

#DESAFIO068 - Jogo PAR OU IMPAR, BREAK QUANDO PERDE

from random import randint

print('VAMOS JOGAR PAR OU ÍMPAR')

resultado = cont = 0 

while True:
    jogoPC = randint(0, 10)
    print(jogoPC)
    jogoJogador = int(input('Valor de 0 a 10: '))
    resultado = jogoPC + jogoJogador
    aposta = ' '
    while aposta not in 'PpIi':
        aposta = str(input('[P]PAR ou [I]Impar? '))

    if aposta in 'Pp' and resultado % 2 == 0:
        print('Você venceu!')
        print(f'Você jogou {jogoJogador} e o computador jogou {jogoPC}. Total {resultado}!')
        print('Vamos jogar novamente...')
        print('=-='*14)
        cont += 1
    
    elif aposta in 'Ii' and resultado % 2 != 0:
        print('Você venceu!')
        print(f'Você jogou {jogoJogador} e o computador jogou {jogoPC}. Total {resultado}!')
        print('Vamos jogar novamente...')
        print('=-='*14)
        cont += 1
    else:
        print('Você PERDEU!')
        print(f'Você jogou {jogoJogador} e o computador jogou {jogoPC}. Total {resultado}!')
        print('^^^^^'*14)
        break
print(f'Você venceu {cont} partidas consecutivas')
print('FIM DO JOGO')

#DESAFIO069 LEIA IDADE E SEXO . A CADA USUARIO DIZER SE QUER CONTINUAR OU NAO. NO FINAL INFORME A) QUANTOS TEM MIAS DE 18 B) QUANTOS HOMENS
# C) QUANTAS MULHERES COM MENOS DE 20

print('-='*4,'CADASTRO INDIVIDUOS','-='*4, '\n' )

maiores = totalHomens = mulherMenos20 = total = 0
while True:
    idade = int(input('Informe idade do indivíduo: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Masculino ou Feminino [M/F]: ')).strip().upper()[0]
    total += 1    

    if idade >= 18:
        maiores += 1
    
    if sexo in 'Mm':
        totalHomens += 1
    
    if sexo in 'Ff' and idade < 20:
        mulherMenos20 += 1
    
    proximo = ' '
    while proximo not in 'SsNn':
        proximo= str(input('Deseja continuar cadastrando [S/N]')).strip().upper()[0]
    if proximo in 'Nn':
        break
print(f'Foram cadastradas {total} pessoas')
print(f'Há {maiores} maiores de 18 anos')
print(f'Há {totalHomens} homens')
print(f'Há {mulherMenos20} mulheres com menos de 20 anos')

#DESAFIO070 leia o nome e preço de produtos. o programa deve perguntar se quer continuar.
#ao final A) total da compra B)quantos custam mais que 1000 C) qual o pruduto mais barato

print('-='*4,'COMPRA DE PRODUTOS','-='*4, '\n' )

precoTotal = custamMaisMil  = c =  0
maisBarato = ' '

while True:
    produto = str(input('Produto: '))
    preco = float(input('Preço: R$ '))
    print('=='*15)
    c += 1

    precoTotal += preco

    if preco > 1000:
        custamMaisMil += 1

    if c == 1:
        menorPreco = preco
        maisBarato = produto
    else: 
        if preco < menorPreco:
            maisBarato = produto
            menorPreco = preco


    continuar = ' '
    while  continuar not in 'SsNn':
        continuar = str(input('Cadastrar próximo produto: [S/N]: '))

    if continuar in 'Nn':
        break

    
    
print(f'Foram cadastrados {c} produtos')
print(f'Valor total da compra: R$ {precoTotal:.2f} reais')
print(f'{custamMaisMil} produtos custam mais que R$ 1000 REIAS')
print(f'O produto mais barato foi {maisBarato} custando R$ {menorPreco:.2f} REIAS')

#DESAFIO071 Simulador CAIXA ELETRONICO. Pergunte valor a ser sacado, progrma vai informar quantas cedulas e seus valores serão entregue
# considere 50, 20, 10, 1

