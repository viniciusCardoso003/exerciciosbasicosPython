#DESAFIO073 - numeros por extenso

extenso = ('zero', 'um', 'dois', 'três','quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze')

while True:
    n = int(input(f'Digite valor de 0 a {len(extenso)-1}: ')) 

    while n not in range (0,len(extenso)):
        n = int(input(f'Tente Novamento. Digite valor de 0 a {len(extenso)-1}: '))
    print(f'Você digitou {n}, {extenso[n]}')
    continuar = ' '
    while continuar not in 'sSnN':
        continuar = str(input('Continuar? [S/N]'))

    if continuar in 'Nn':
        break    

print('fim')

#DESAFIO073 - tupla com 20 times. A) 5 primeiros. B) 4 ultimos c) ordem albetica b)posição Cuiabá

times = ('Santos', 'São Paulo','Palmeiras','Corinthians','Fluminense','Botafogo','Vasco da Gama','Flamengo',
'Internacional','Grêmio','América-MG','Cruzeiro','Atlético-MG','Atlético-PR','Coritiba','Cuiabá','Bahia',
'RB Bragentino','Fortaleza', 'Goiás')

print(f'Lista de Times:')
for time in times:
    print(f'{times.index(time)+1}ª {time}')

print('=-=-'*22)
print(f'Os 5 primeiros são:{times[0:5]}')
print('=-=-'*22)
print(f'Os 4 últimos são:{times[16:]}')
print('=-=-'*22)
print(f'Ordem Alfabética: {sorted(times)}')  

print(f'O Cuiabá está na {times.index('Cuiabá')+1}ª posição')

#COMPLEMENTO, EM QUE POSIÇÃO ESTÁ TAL TIME

times = ('Santos', 'São Paulo','Palmeiras','Corinthians','Fluminense','Botafogo','Vasco da Gama','Flamengo',
'Internacional','Grêmio','América-MG','Cruzeiro','Atlético-MG','Atlético-PR','Coritiba','Cuiabá','Bahia',
'RB Bragantino','Fortaleza', 'Goiás')

while True:
    clube = ' '
    while clube not in times:
        clube = str(input('Deseja saber a posição de qual Clube: '))
    print(f'{clube} está na {times.index(clube)+1}º posição')

    c = ' '
    while c not in 'SsNn':
        c = str(input('Deseja parar? [S/N]'))
    if c in 'Ss':
        break
print('FIM')

#DESAFIO074 maior e menores valores em Tuplas
from random import randint

n = (randint(0,10), randint(0,10),randint(0,10),randint(0,10),randint(0,10))

print(f'Valores Sorteados:')
for elemento in n:
    print(f'{elemento}', end =' ')
print(f'\nO maior valor é {max(n)}')
print(f'O menor valor é {min(n)}')

#DESAFIO075 analise de dados em python A) QUANTAS VEZES APARECEU 9 B) EM QUE POSIÇÃO FOI DGITADO VALOR 3 C) QUAIS SÃO PARES
num = ( int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')) )


totalNove = pares = posicao3 = 0

print('Números Digitados:')
for n in num:
    print(f'{n}', end=' ')

    if n == 9:
        totalNove += 1

    if n % 2 == 0:
        pares += 1

print(f'\nForam digitados {totalNove} números NOVE!')
print(f'Foram digitados {pares} pares')
if 3 in num:
    print (f'O número 3 está na {num.index(3)+1}ª posiçao')
else:
    print('Não há nenhum número 3 na Tupla')  
    
#GABARITO
num = ( int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')) )


print(f'Números Digitados: {num}')

#A)QUANTAS VEZES APARECEU 9
if num.count(9) == 1:
    print('O número 9 foi digitado apenas 1 vez')
else:
    print(f'Foram digitados {num.count(9)} números NOVE!')

#B) QUAIS SÃO PARES

pares = 0

for n in num:
    if n % 2 == 0:
        pares += 1

if pares == 0:
    print('Não há nenhum número par')
else:
    print('Os valores pares digitados foram: ', end = ' ')
    for n in num:
        if n % 2 == 0:
            print(n, end = ' ')

#C)EM QUE POSIÇÃO FOI DIGITADO VALOR 3
if 3 in num:
    print (f'\nO número 3 está na {num.index(3)+1}ª posiçao pela primeira vez')
else:
    print('\nNão há nenhum número 3 na Tupla') 
    
    
#DESAFIO076 - lista de preços com Tuplas
produtos = ('Notebook',2500, 'Mouse', 120, 'Teclado',200, 'Câmera',500,
            'Impressora', 1800 )

total = 0

print('=='*23)
print(f'{"Lista Compras":^40}')
print('=='*23)
for pos in range (0,len(produtos)):
    if pos % 2 == 0:
        print(f'Produto: {produtos[pos]:.<20}', end = ' ')
    else:
        print(f'R$ {produtos[pos]:>.2f} reias')
        total += produtos[pos]
print('=='*23)
print(f'TOTAL: R$ {total:.2f} reais')

#Tentativa com duas listas

produtos = ('Notebook', 'Mouse', 'Teclado', 'Câmera')
preços = (2500, 120, 200, 500)
total = 0

print('=='*20)
print('==='*4, 'Lista Compras', '==='*4)
print('=='*20)
for c in range (0,len(produtos)):
    print(f'Produto: {produtos[c]:.<20} R$ {preços[c]} reias')
    total += preços[c]
print('=='*20)
print(f'TOTAL: R$ {total:.2f} reais')

#AULA 17 COMANDOS COM LISTAS

num = [0, 5, 8, 9]
num[0] = 7
num.append(10)
num.sort()
num.sort(reverse=True)
num.insert(3, 12)
num.pop(2)
num.remove(9)

print(num)
print(f'Essa lista tem {len(num)} elementos')

#//////////
valores = []

for c in range (0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c+1} encontrei o valor {v}!')
    
#Cópia de listas
a = [2, 5, 7, 10]
b = a[:]
b[0] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')    

#DESAFIO078 maior e menores valores na lista 
lista = list()

for c in range (0,5):
    lista.append(int(input(f'Digite o {c + 1}ª valor: ')))
print(f'O Maior valor é: {max(lista)}, e esta na posição', end = ' ')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end = '')
print(f'\nO Menor valor é: {min(lista)}, e esta na posição', end = ' ')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end = ' ')
        
#DESAFIO079 Valores únicos em uma lista
lista = []

while True:
    num = int(input('Digite o valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com SUCESSO...')
    else:
        print('Valor duplicado. NÃO adicionado na lista...')
    
    prox = ' '
    while  prox not in 'SsNn':
        prox = str(input('Deseja continuar? [S/N]'))

    if prox in 'Nn':
        break

print(sorted(lista))

#DESAFIO080 leia 5 valores númericos cadastre os em uma lista, já na posiçao correta se usar o sort

lista = []

for c in range (0,5):
    n = int(input('Informe um valor: '))
    if n == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else: 
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos +=1
print('=='*20)
print(f'Os valores adicionados foram {lista}')

#DESAFIO081 leia numeros e coloque na lista a) quantos foram digitados b) lista em ordes DECRESCENTE c) valor 5 está ou não na lista

lista = []


while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    print(f'Valor {n} adicionado à lista...')
    prox = ' '
    while prox not in 'SsNn':
        prox = str(input('Deseja continuar? [S/N]'))
    if prox in 'Nn':
        break
print('=='*20)
print(f'{len(lista)} Valores adicionados \n{lista}')

if 5 not in lista:
    print('Não há valor 5 na lista')
else:
    print(f'O número 5 aparece na lista na posição: ', end = ' ')
    for c, v in enumerate(lista):
        if v == 5:
            print(f'{c}...', end = ' ')
    
lista.sort(reverse=True)
print()
print(f'Os valores em ordem decrescente são: {lista}')

#DESAFIO082 leia varios números e coloque em listas 3 listas. lista geral, lista de pares e lista de impares
pares = []
impares = []
geral = []

while True:
    n = int(input('Valor: '))
    geral.append(n)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    prox = ' '
    while prox not in 'SsNn':
        prox = str(input('Continuar? [S/N]'))
    if prox in 'nN':
        break
print(f'Lista de Geral: {geral}')
print(f'Lista de Pares: {pares}')
print(f'Lista de ímpares: {impares}') 

#DESAFIO084. leia nome e peso. guarde tudo em uma lista . mostre a) quantas pessoas cadastradas b) pessoas mais pesadas c) pessoas mais leves 
cadastro = []
dados = []
maior =  menor = 0
nomeMenor = nomeMaior = ' '

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    if len(cadastro) == 0:
        maior = menor = dados[1]
        nomeMaior = nomeMenor = dados[0]
    else: 
        if dados[1] > maior:
            maior = dados[1]
            nomeMaior = dados[0]

        if dados[1] < menor:
            menor = dados[1]
            nomeMenor = dados[0]

    cadastro.append(dados[:])
    dados.clear()

    prox = ' '
    while prox not in 'SsNn':
        prox = str(input('Continuar? [S/N]: '))

    if prox in 'Nn':
        break

print('=='*15)
print(f'Foram cadastradas {len(cadastro)} pessoas')
print('=='*15)
print(cadastro)
print('=='*15)
print(f'O maior peso foi de {nomeMaior}, com {maior} kg')
print(f'O menor peso foi de {nomeMenor}, com {menor} kg')

#DESAFIO084 CORRIGIDO

cadastro = []
dados = []
maior =  menor = 0
nomeMenor = nomeMaior = ' '

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    if len(cadastro) == 0:
        maior = menor = dados[1]
        nomeMaior = nomeMenor = dados[0]
    else: 
        if dados[1] > maior:
            maior = dados[1]
            nomeMaior = dados[0]

        if dados[1] < menor:
            menor = dados[1]
            nomeMenor = dados[0]

    cadastro.append(dados[:])
    dados.clear()

    prox = ' '
    while prox not in 'SsNn':
        prox = str(input('Continuar? [S/N]: '))

    if prox in 'Nn':
        break

print('=='*15)
print(f'Foram cadastradas {len(cadastro)} pessoas')
print('=='*15)
print(cadastro)
print('=='*15)
print(f'O maior peso foi de {maior}kg. Pertencente -->', end =' ')
for p in cadastro:
    if p[1] == maior:
        print(f'{p[0]}...', end =' ')
print()
print('=='*15)
print(f'O menor peso foi de {menor}kg. Pertencente -->', end=' ')
for p in cadastro:
    if p[1] == menor:
        print(f'{p[0]}...', end=' ')
        
#DESAFIO085 - leia varios valores e divida-os em duas listas diferentes dentro de uma unica lista
geral = [[],[]]

for c in range (0,7):
    n = int(input(f'Informe o {c+1}º termo: '))
    
    if n % 2 == 0:
        geral[0].append(n)
    else:
        geral[1].append(n)

print(f'GERAL: {geral}')
print(f'PARES: {sorted(geral[0])}')
print(f'ÍMPARES: {sorted(geral[1])}')

#DESAFIO086 Matriz 3 x3, mostrar na formatação correta
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Informe valor para [{l}] e [{c}]:'))
print('=='*20)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end = ' ')
    print()

#DESAFIO087. aprimnore anterior a) a soma dos pares digitados b) a soma dos valores da terceira coluna c) o maior valor da segunda linha
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
pares = totalTercColuna = maiorSegundaLinha = 0

for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Informe valor para [{l}] e [{c}]:'))

        if c == 2:
            totalTercColuna += matriz[l][2]

        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        
        if l == 1 or matriz[1][c] > maiorSegundaLinha : 
            maiorSegundaLinha = matriz[1][c]



print('=='*20)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end = ' ')
    print()

print('=='*20)

print(f'A soma dos números pares foi: {pares}')
print(f'A soma dos valores na terceira coluna foi: {totalTercColuna}')
print(f'O maior valor na segunda linha é: {maiorSegundaLinha}')

#DESAFIO088 - crie palpites da mega sena. Número de 1 a 60. programa pergunta quantos jogos serão gerados
from random import randint
from time import sleep

print('LOTERIAS PALPITES')

n = int(input('Deseja simular quantos jogos? '))

for c in range (1,n+1):
    jogo = [randint(1,60), randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60),]
   
    print(f'{c}ª Palpite: {sorted(jogo)}')
    sleep(1.5)
print('FIM')

#CORRIGIDO

from random import randint
from time import sleep

print('LOTERIAS PALPITES')
print('=='*30)
quant = int(input('Número de jogos: '))
print('=='*30)


jogos = []
lista = []
total = 0

while total < quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.append(lista[:])
    total += 1
    lista.clear()
    
print('=='*30)
print(f'-----MOSTRANDO {total} PALPITES-----')
print('=='*30)

for c in range (0,total):
    print(f'{c+1}ª Aposta: {jogos[c]}')
    sleep(1.5)
    

#DESAFIO089

ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1+nota2)/2

    ficha.append([nome, [nota1, nota2], media])

    proximo = ' '
    while proximo not in 'SsNn':
        proximo= str(input('Deseja continuar cadastrando [S/N]')).strip().upper()[0]
    if proximo in 'Nn':
        break

print('=='*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('--'*16)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

print('=='*30)

while True:
    opc = int(input('Mostrar notas de qaul aluno ? [999 interrompe]: '))
    if opc == 999:
        break
    if opc <= len(ficha):
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
    
#DESAFIO090 leia nome e media de aluno. no final mostre os valores e se foi aprovado recuperção ou reprovado
ficha = {
    'nome': str(input('Inform nome: ')),
    'media': float(input('Informe média: '))  
}
print('=='*15)

for k, v in ficha.items():
    print(f'- O {k} é {v}')

if ficha['media'] > 7:
    print('- situação APROVADO')
elif ficha['media'] < 5:
    print('- situação REPROVADO')
else:
    print('- situação RECUPERAÇÃO')
    
#DESAFIO090 MELHORADO
    
listaGeral = []

print('SISTEMA DE NOTAS DE ALUNOS')
print()

while True:
    ficha = {
        'nome': str(input('Inform nome: ')),
        'nota1': float(input('Informe nota1: ')),
        'nota2': float(input('Informe nota2: ')),
    }

    media = (ficha['nota1'] + ficha['nota2'])/2
    ficha['media'] = media

    if media > 6:
        ficha['situação'] = 'APROVADO'
    elif media <= 4:
        ficha ['situação'] = 'REPROVADO'
    else:
        ficha['situação'] = 'RECUPERAÇÃO'
    
    listaGeral.append(ficha.copy())
    ficha.clear()

    print('=='*15)
    prox = ' '
    while prox not in 'SsNn':
        prox = str(input('Próximo ? [S/N]'))
        print()

    if prox in 'Nn':
        break

print('\nRESULTADOS ABAIXO')
print('=='*15)
for f in listaGeral:
    for k, v in f.items():
        print(f'{k}: {v}')
    print('--'*15)
    
#DESAFIO091 4 JOGADORES JOGUEM UM DADO E TENHAM RESULTADOS ALEATÓRIOS. GUARDE NO DICIONARIO. NO FINAL COLOQUE O DICIONARIO EM ORDEM
from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)
}

ranking = list()
print('SORTEANDO DADOS...')
sleep(1)
print('3...')
sleep(1)
print('2...')
sleep(1)
print('1...')
sleep(1)

print('VALORES SORTEADOS')
sleep(1)
for k, v in jogo.items():
    print(f'{k} sorteou -> {v}')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-----CLASSIFICAÇÃO-----')
for i, v in enumerate(ranking):
    print(f'{i+1}ª lugar: {v[0]} com {v[1]} pontos')

#DESAFIO092 LEIA NOME, ANO NASC. E CARTEIRA TRABALHO E CADASTRE-OS (COM IDADE) NUM DICIONÁRIO, SE A CT FOR DIF DE 0
# O DICIONARIO RECEBERÁ ANO DA CONTRAÇÃO E SALÁRIO. CALCULE E ACRESCENTE ALÉM DA IDADE, COM QUANTOS ANOS A PESOA VAI SE APOSENTAR

from datetime import date

lista = []

while True:

    individuo ={}

    nome = str(input('Nome: '))
    individuo['nome'] = nome

    anoNascimento = int(input('Ano Nascimento: '))
    atual = date.today().year
    idade = atual - anoNascimento
    individuo['idade'] = idade 

    CTPS = 0
    while CTPS == 0:
        CTPS = int(input('Nº Carteira Profissional: '))
    
    if CTPS != 0:
        individuo['carteira profissional'] = CTPS
        anoContratacao = int(input('Ano Contratação: '))
        mediaSalarial = float(input('Média Salarial: '))
        individuo['ano contratação'] = anoContratacao
        individuo['media salarial'] = mediaSalarial
     

    tempoContribuicao = atual - anoContratacao
    individuo['atual tempo contribuiçao'] = tempoContribuicao 

    anosParaAposentar = 35 - tempoContribuicao
    idadeAposentar = idade + anosParaAposentar
    individuo['Idade prevista aposentadoria'] = idadeAposentar 

    if tempoContribuicao >= 35:
        individuo['situação'] = 'APOSENTADO'
    elif tempoContribuicao < 35:
        individuo['situação'] = 'CONTRIBUINTE'

    lista.append(individuo.copy())

    prox = ' '
    while prox not in 'SsNn':
        prox = str(input('Próximo ? [S/N]'))
    
    if prox in 'Nn':
        break

print('==='*25)
print('RESULTADOS ABAIXO:')
print('---'*16)
for i in lista:
    for k, v in i.items():
        print(f'{k}: {v}')
    print('---'*16)

#DESAFIO093 - APROVEITAMENTO JOGADOR. LEIA NOME , PARTIDAS E GOLS. GUARDE NUM DICIONÁRIO INCLUINDO TOTAL DE GOLS FEITOS
print('----- RANKING ATACANTEs MÉDIA DE GOLS----')

lista = []

while True:

    jogador = {'Nome': str(input('Nome: ')),
               'TotalJogos': int(input('Número de jogos: '))
                }

    gols = 0
    if jogador['TotalJogos'] == 0:
        jogador['Gols'] = 0
        jogador['Media'] = 0

    elif jogador['TotalJogos'] > 0:
        for g in range (0, jogador['TotalJogos']):
            gol = int(input(f'Gol feitos no {g+1}ª jogo: '))
            gols += gol


        jogador['Gols'] = gols
        media = gols/ jogador['TotalJogos']
        jogador['Media'] = media
    
    lista.append(jogador)

    
    prox = ' '
    while prox not in 'NnSs':
        prox = str(input('Continuar? [S/N]'))

    if prox in 'Nn':
        break

print('===RESULTADOS===')
for j in lista:
    for k, v in j.items():
        print(f'{k}: {v}')
    print('--'*10)
    
 #corrigido
 
 jogador = {}
partidas = []

jogador['Nome'] = str(input('Nome: '))

total = int(input(f'Quantas partidas {jogador['Nome']} jogou: '))

for j in range(0, total):
    partidas.append(int(input(f'Gols no {j+1} jogo? ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*12)
print(jogador)
print('===='*10)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('===='*10)

print(f'{jogador["Nome"]} atuou em {total} partidas')
for g in range (0, len(partidas)):
    print(f'  => Jogo: {g}: {partidas[g]} gols')
print(f'TOTAL: {jogador["total"]} gols.')
mediaGols = jogador['total']/total 
print(f'Média de {mediaGols:.2f} gols por jogo.')

#DESAFIO094 - LEIA NOME, SEXO E IDADE. GUARDE EM DICT E TODOS EM LIST. MOSTRE A) QUANTAS PESSOAS CADASTRADAS
#B) LISTA COM MULHERES C) PESSOAS COM IDADE ACIMA DA MEDIA

lista = []

totalPessoas = somaIdades = 0
while True:
    dados = {}

    dados['nome'] = str(input('Nome: '))
    dados['idade'] = int(input('Idade: '))
    somaIdades += dados['idade']

    
    while True: 
        dados['sexo'] = str(input('Sexo: [F/M]: ')).upper()[0]
        if dados['sexo'] in 'MmFf':
            break
        print('ERRO! digite somente M ou F')

    totalPessoas += 1
    lista.append(dados.copy())

    while True:
        cont = str(input('Continuar? [S/N]')).upper()[0]
        if cont in 'SN':
            break
        print('ERRO! RESPONDA S ou N..')
    if cont in 'Nn':
        break
print('===='*15)

print(f'TOTAL DE PESSOAS CADASTRADAS: {totalPessoas}')
media = somaIdades/totalPessoas
print(f'MEDIA DE IDADE: {media:.2f}')
print('===='*15)

print('LISTA DE MULHERES:', end=' ')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p['nome']},', end=' ')
print()
print('===='*15)

acimaDaMedia = 0
print('Pessoas com idade acima da média: ')
for p in range(0,len(lista)):
    if lista[p]['idade'] > media:
        print(f' => {lista[p]['nome']} com {lista[p]['idade']} anos/idade')
        acimaDaMedia =+ 1

if acimaDaMedia == 0:
    print(' => Não nenhuma pessoa com idade acima da média')

#DESAFIO096 função que calcule a área de um espaço
def calculoArea(largura = float(input('LARGURA (m): ')),comprimento = float(input('COMPRIMETO (m): '))):
    print('CALCULO DE ÁREA')

    print('===='*10)
    print(f'A área é igual a: {largura*comprimento} metros²')

calculoArea()

#DESAFIO097 texto qualquer como parametro e mostre uma mensagem com tamanho adaptável
def escreva(msg):
    tam = len(msg) + 4
    print('='*tam)
    print(f'  {msg}')
    print('='*tam)


escreva('OLÁ')
escreva(' TITULO GRANDE')

#DESAFIO098 função contador, receba 3 parametros(inicio, fim e passo). realize 3 contagens:a) de 1 a 10, de 1 em 1 
#b) de 10 a 0, 2 em 2 c) personalizada 
from time import sleep

def titulo (msg):
    print('=='*20)
    print(msg)
    print('=='*20)

def contador (inicio, passo, fim):
    if passo < 0:
        passo = passo * (-1) 
    if passo == 0:
        passo = 1
    sleep(2.5)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end= ' ', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end = ' ', flush=True)
            sleep(0.5)
            cont -= passo 
        print('FIM!')


titulo('Contando de 0 a 10...')
contador(0,1,10)

titulo('Contando de 10 a 0...')
contador(10,1,0)

print('---'*15)
titulo('Agora é sua vez de personalizar: ')

i = int(input('Número Inicial: '))
f = int(input('Número Final: '))
p = int(input('Passo: '))

titulo(f'Contando de {i} até {f} com passo {p}...')
contador(i,p,f)



#DESAFIO099 Faça um programa que tenha uma função chamada maior(), 
#que receba vários parâmetros com valores inteiros. 
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior ():
    lista = []
    for x in range (1,4):
        n = int(input(f' Valor de {x}° numero: '))
        
        lista.append(n)
        
    print('NÚMEROS DIGITADOS...')
    for x in range (0, len(lista)):
        print(f'{lista[x]}', end = ' ')      
    
    print('\n-----------')
    print(f'Foram informados {len(lista)} valores')
    print(f'A maior número digitado foi {max(lista)}. ')


maior()

#correção

def maior (* num):
    cont = maior = 0
    print('Analisando os valores:', end =' ')
    for n in num:
        print(f'{n}', end = ' ')
        if cont == 0 or n > maior:
            maior = n
        cont += 1
    print()
    print(f'Foram informados {cont} valores')
    print(f'O maior valor foi {maior}')
    print('===========================')

maior(12, 56, 200, 56, 78, 89)

maior()

maior(12, 0, 67, 100)

#DESAFIO100 um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
#e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

def linha ():
    print('\n=========================')

def sorteia (lista):
    print('NÚMEROS SORTEADOS: ', end = ' ', flush=True)
    sleep(1)
    for x in range (0,5):
        x = randint(0,10)
        print(f'{x}', end = ' ', flush=True)
        sleep(0.5)
        lista.append(x)
    linha()

def somaPar (lista):
    pares = 0
    print('Os números pares são:', end = ' ')
    for x in lista:
        if x %  2 == 0:
            print(f'{x}', end = ' ')
            pares += x
    print(f'\nA Soma dos pares foi igual a: {pares}')
    

numeros = []
sorteia(numeros)
somaPar(numeros)

#aula 21
#FUNÇÕES COM DOCUMENTAÇÃO

from time import sleep

def titulo (msg):
    """
    -> Função titulo exibe mensagem de titulo com borda em '=='
    :param msg: recebe mensagem a ser mostrada
    Função criada por Vinicius Cardoso
    """
    print('=='*20)
    print(msg)
    print('=='*20)

def contador (inicio, passo, fim):
    """
    -> faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param p: passo da cntagem
    :param f: fim da contagem
    return: sem retorno
    Função criada por Vinicius Cardoso
    """
    if passo < 0:
        passo = passo * (-1) 
    if passo == 0:
        passo = 1
    sleep(2.5)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end= ' ', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end = ' ', flush=True)
            sleep(0.5)
            cont -= passo 
        print('FIM!')


titulo('Contando de 0 a 10...')
contador(0,1,10)

titulo('Contando de 10 a 0...')
contador(10,1,0)

print('---'*15)
titulo('Agora é sua vez de personalizar: ')

i = int(input('Número Inicial: '))
f = int(input('Número Final: '))
p = int(input('Passo: '))

titulo(f'Contando de {i} até {f} com passo {p}...')
contador(i,p,f)

help(contador)

#aula 21

def fatorial (n=1):
    """
    -> Calcula Fatorial de n.
    :param n: início da contagem
    Função criada por Vinicius Cardoso
    """
    f =1 
    for c in range(n,0,-1):
        f *= c
    return f

n = int(input('Valor? '))
f1 = fatorial(n)
print(f'O fatorial de {n} é {fatorial(n)}')

def parOuImpar (n=0):
    """
    -> Informa se n é par oou ímpar.
    :param n: valor de n
    :return:se n é par ou ímpar 
    Função criada por Vinicius Cardoso
    """
    
    if n % 2 == 0:
        return (print(f'{n} é par'))
    else:
        return (print(f'{n} é ímpar'))

def par(n=0):
    """
    -> Informa se n é par ou ímpar
    :param n: valor de n 
    Função criada por Vinicius Cardoso
    """
    if n % 2 == 0:
        return True
    else:
        return False



parOuImpar(5)
print(par(5))

#DESAFIO101 - FUNÇÕES POR VOTAÇÃO 

from datetime import date

def voto(anoNascimento):
    anoAtual = date.today().year
    idade = anoAtual - anoNascimento
    if idade < 15:
        return print(f'Idade: {idade}. NÃO VOTA.')
    elif idade >= 15 and idade < 18:
        return print(f'Idade: {idade}. VOTO OPCIONAL')
    elif idade >= 18 and idade <= 65:
         return print(f'Idade: {idade}. VOTO OBRIGATÓRIO')
    else:
        return print(f'Idade: {idade}. VOTO OPCIONAL')

#DESAFIO102 - rograma que tenha uma função fatorial() que receba dois parâmetros: 
#o primeiro que indique o número a calcular e outro chamado show, 
#que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial

def fatorial (n=0, show=False):
    """
    -> Calcula fatorial de um número.
    :param n: o número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return:o valor do Fatorial de um numero n
    """
    f = 1 
    for c in range(n,0,-1):
        if show:
             print(c, end = '')
             if c > 1:
                 print(' x ', end = '')
             else:
                print(' = ', end = '')
        f *= c
    return print(f)


fatorial(4, show=True)

fatorial(4)

#DESAFIO103 - programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
#o nome de um jogador e quantos gols ele marcou. 
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='<desconhecido>', gols = 0):
    """
    -> Função ficha, informa nome e quantidade de gols de jogador
    :param1: nome do jogador
    :param2: quantidade de gols
    return: print(f'Jogador {nome}, marcou {gols} gols. ')
    """
    def cont():
	print('-'*35)
	nome=str(input('Nome do jogador: '))
	if len(nome) == 0:
		nome='<Desconhecido>'
	gols=str(input('Número de gols: '))
	if len(gols) == ' ' or gols != int:
		gols = 0
	print(f'O jogador {nome} fez {gols} gol(s) em um campeonato.')

cont()

#DESAFIO104- um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, 
#só que fazendo a validação para aceitar apenas um valor numérico.


def leiaInteiro():
    while True:
        print('-'*35)
        n = input('Valor de N: ')
        if n.isnumeric() :
            return f'\033[36m{n}\033[m'
            #formatação em CIANO
        else:
            print('')
            #formatação em VERMELHO

print(f'Você digiotu o número n: {leiaInteiro()}')

"""
CALCULADORA COM EXCEPTIONS \033[31mERRO! Digite um número válido\033[m
"""
operadoresValidos = '+/-*'

try:
    while True:
        n1 = int(input('Informe primeiro Valor: '))
        n2 = int(input('Informe segundo Valor: '))
        while True:
            operador = str(input('Qual operação? '))[0]
            if operador in operadoresValidos:
                break
            print('\033[31mERRO! Digite apenas um operador válido\033[m')
        
        if operador == '+':
            resultado = n1 + n2 

        elif operador == '-':
            resultado = n1 - n2

        elif operador == '*':
            resultado = n1 * n2 

        elif operador == '/':
            resultado = n1 / n2
        print('\033[31mRESULTADO\033[m')
        print(f'{n1} {operador} {n2} = {resultado}')

        while True:
            continuar = str(input('Deseja continuar? ')).upper()[0]
            if continuar in 'SN':
                break
            print('ERRO! RESPONDA S ou N..')
        if continuar in 'N':
            break
    print('=====================')

except:
    print('Algum dos nomeros está errado')
    

#DESAFIO114 site está acessível
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except:
    print('DEU ERRO')
else:
    print('TUDO OK')
    print(site.read())

