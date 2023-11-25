#BALANÇO PATRIMONIAL

print('BALANÇO PATRIMONIAL')

historicoContas = []
bensDireitos = obrigações = balanco = 0

while True: 
    contas = {
        'Titulo da Conta': str(input('Titulo da conta: ')),
        'Valor da Conta': float(input('Valor da conta: R$ '))
    }

    tipoConta = ' '
    while tipoConta not in 'OobBdD':
        tipoConta = str(input('Tipo da Conta:\n[B]BEM\n[D]Direito\n[O]Obrigação\n Qual Opção? '))
    
    contas['Tipo da Conta'] = tipoConta

    if contas['Tipo da Conta'] in 'Bb' or contas['Tipo da Conta'] in 'Dd':
        bensDireitos += contas['Valor da Conta']
    

    elif contas['Tipo da Conta'] in 'Oo':
        obrigações += contas['Valor da Conta']
    
    if tipoConta in 'Bb':
        contas['Tipo da Conta'] = 'BEM'
    elif tipoConta in 'Dd':
        contas['Tipo da Conta'] = 'DIREITO'
    elif tipoConta in 'oO':
        contas['Tipo da Conta'] = 'OBRIGAÇÃO'

    
    historicoContas.append(contas.copy())
    contas.clear()

    prox = ' '
    while prox not in 'SsNn':
        prox = str(input('Continuar?[S/N]'))
    
    if prox in 'nN':
        break

print('==='*20)
for c in historicoContas:
    for k, v in c.items():
        print(f'{k}: {v}')
    print('--'*12)
print('==='*20)

balanco = bensDireitos - obrigações

print('------RESULTADOS DO BALANÇO PATRIMONIAL-------')
print()
print(f'PATRIMÔNIO BRUTO: R$ {bensDireitos} reais')
print(f'OBRIGAÇÕES: R$ {obrigações} reais')

if balanco > 0: 
    print(f'Balanço fechado em R$ {balanco} REAIS')
    print('===>POSITIVO')
elif balanco < 0:
    print(f'Balanço fechado em R$ {balanco} REAIS')
    print('===>NEGATIVO')
else:
    print('===>SALDO NULO')
    
#CADASTRO USANDO FUNÇÕES E LISTA E DICIONARIOS

listaAlunos = []

def cadastroAluno(nome, modalidade):
    aluno = {
        'Nome': nome,
        'Modalidade': modalidade
    }

    listaAlunos.append(aluno.copy())

while True:
    cadastroAluno(str(input('NOME: ')), str(input('MODALIDADE: ')))

    while True: 
        prx = str(input('Continuar? ')).upper()[0]
        if prx in 'SN':
            break
        print('ERRO! RESPONDA S ou N..')
    if prx in 'N':
        break

print(listaAlunos)

#CORES TERMINAL 

#PRECEDENCIA DE OPERADORES
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)

"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = 'CARLOS'
idade = 56

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'Seu nome invertido é: { nome[::-1]}')
    print(f'A primeira letra é: {nome[0]}')
    if ' ' in nome:
        print('Seu nome CONTÉM espaços')
    else:
        print('Seu nome NÃO CONTÉM espaços')
    print(f'A ultima letra do seu nome é: {nome[-1]} ')
else:
    print('CAMPOS VAZIOS')
    
"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = 'gato'.upper()
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ').upper()[0]
    numero_tentativas += 1


    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letraSecreta in palavra_secreta:
        if letraSecreta in letras_acertadas:
            palavra_formada += letraSecreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0

##FUNÇÃO PARA ADICIONAR VEICULOS EM ESTOQUE - FUNÇÃO, LISTA E DICT
        
        
estoque = [{'Nome': 'Siena', 'Ano': 2002, 'Preco': 1}]


def adicionar_ao_estoque():
    total_estoque = 0
    while True:
        produto = {}
        produto['Nome'] = str(input('Nome do Veículo: '))
        produto['Ano'] = int(input('ANO: '))
        produto['Preco'] = float(input('Preco: '))
        estoque.append(produto.copy())

        while True:
            prox = str(input('Continuar?[S/N] ')).upper()
            if prox in 'SN':
                break
        if prox == 'N':
            for carro in estoque:
                if carro['Preco']:
                    total_estoque += carro['Preco']
            break

    return print(estoque, total_estoque)


adicionar_ao_estoque()


'''Crie uma função “verificar_senha” no qual retorna true caso a senha inserida for
correta e false caso o contrário. Logo após elabore um “mini-sistema” de checar a
senha inserida, onde o usuário tem 3 tentativas de senha e caso esse número seja
ultrapassado o programa é encerrado.'''

cadastro = [{'nome': 'Carlos', 'senha': 1234},{'nome': 'Joana', 'senha': 1235} ]


print('SISTEMA DE LOGIN')

def check_password():
    tentativas = 4
    while True:
        validacao = {}
        validacao['nome'] = str(input('Nome: '))
        validacao['senha'] = int(input('Senha: '))

        if validacao not in cadastro:
            tentativas -= 1
            if tentativas > 0:
                print(f'ACESSO NEGADO, você possui mais {tentativas} tentativas')
                print()
            if tentativas == 0:
                print('CONTA BLOQUEADA...')
                break
        else:
            print('ACESSO LIBERADO')
            break
    if validacao in cadastro:
        return True
    else:
        return False

if check_password() is True:
    print('PROGRAMA DISPONIVEL')
else:
    print('FIM')
    
'''O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, 
que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, 
de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo'''

preco_unitário = 0.18

print('Panificadora Pão de Ontem - Tabela de preços')

for c in range(50):
    print(f'Qtd: {c+1}  R$ {(c+1)*preco_unitário:.2f}')    


'''O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de bebidas. 
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber o CÓDIGO e a Quantidade do produto. 
O programa deve então mostrar o total da compr. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. 
A saída deve ser conforme o exemplo abaixo:'''


estoque = [{'cod':1, 'produto': 'Coca-cola', 'preco': 5.00, 'qtd_em_estoque': 50},
           {'cod':2, 'produto': 'Heineken', 'preco': 9.00, 'qtd_em_estoque': 200},
           {'cod':3, 'produto': 'Dolly', 'preco': 3.25, 'qtd_em_estoque': 200}]

def venda():
    total_geral = 0
    lista_compra = []
    while True:
        validacao ={}
        validacao['codigo'] = int(input('Código: '))
        quantidade = int(input('Quantidade: '))

        for p in estoque:
            if validacao['codigo'] == p['cod']:
                p['qtd_em_estoque'] -= quantidade
                total_venda = p['preco'] * quantidade
                total_geral += total_venda

                validacao['produto'] = p['produto']
                validacao['quantidade vendida'] = quantidade
                validacao['preco total'] = total_venda

                lista_compra.append(validacao.copy())
                

        while True:
            cont = str(input('Continuar? [S/N] '))[0].upper()
            if cont in 'SN':
                break
            print('ERRO! Digite SIM ou NÃO')
        if cont == 'N':
            lista_compra.append(total_geral)    
            break

    return lista_compra


lista = venda()

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

#AUMENTO DE PREÇO EM 10%
for p in produtos:
    acrescimo = p['preco'] * 0.1
    preco_acrescido = round(p['preco'] + acrescimo, 2)
    if p['preco']:
        p['preco'] = preco_acrescido

#ADICIONAR NOVO PRODUTO
novo_produto = {'nome': 'Produto 6', 'preco': 190.50}
produtos.append(novo_produto.copy())


#ORDENAR POR ORDEM DECRESCENTE - NOME
produtos_ordenados_nome = sorted(produtos, key=lambda p: p['nome'], reverse=True)

#ORDENAR POR ORDEM CRESCENTE - PREÇO
produtos_ordenados_preco = sorted(produtos, key=lambda p: p['preco'])



