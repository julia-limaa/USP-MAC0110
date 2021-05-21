# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------
     
'''
    Nome: Júlia de Lima Oliveira
    NUSP: 12567082

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''

# escreva seu programa a seguir

n = int(input('Digite n: '))
i = 1
x = n
while x > 9:
    x //= 10
    i += 1
ndig = i
x = n
d = 0
mult = 0
soma = 0
while x > 9:
    d = x % 10
    mult = d*i 
    soma += mult
    x //= 10
    i -= 1
soma = soma + i*x
if soma % 11 == 10:
    dv1 = 0
else: 
    dv1 = soma % 11

i = 1
x = n
while x > 9:
    x //= 10
    i += 1
x = n
d = 0
mult = 0
soma = 0
while x > 9:
    d = x % 10
    mult = d*(i-1) 
    soma += mult
    x //= 10
    i -= 1
soma = soma + ndig*dv1
if soma % 11 == 10:
    dv2 = 0
else: 
    dv2 = soma % 11
print(f'DVs = {dv1} {dv2}')


'''n = int(input('Digite n: '))
i = 1
x = n
while x > 9:
    x //= 10
    i += 1
ndig = i
x = n
d = 0
mult = 0
soma = 0
while x > 9:
    d = x % 10
    print(f'd = {d}')
    mult = d*i 
    print(f'mult = {mult}')
    soma += mult
    print(f'soma = {soma}')
    x //= 10
    print(f'x = {x}')
    i -= 1
    print(f'i = {i}')
soma = soma + i*x
if soma % 11 == 10:
    dv1 = 0
else: 
    dv1 = soma % 11
print(f'd = {d}')
print(f'x = {x}')
print(f'i = {i}')
print(f'mult = {mult}')
print(f'soma = {soma}')
print(f'dv1 = {dv1}')

i = 1
x = n
while x > 9:
    x //= 10
    i += 1
x = n
d = 0
mult = 0
soma = 0
while x > 9:
    d = x % 10
    print(f'd = {d}')
    mult = d*(i-1) 
    print(f'mult = {mult}')
    soma += mult
    print(f'soma = {soma}')
    x //= 10
    print(f'x = {x}')
    i -= 1
    print(f'i = {i}')
soma = soma + ndig*dv1
if soma % 11 == 10:
    dv2 = 0
else: 
    dv2 = soma % 11
print(f'd = {d}')
print(f'x = {x}')
print(f'i = {i}')
print(f'mult = {mult}')
print(f'soma = {soma}')
print(f'dv2 = {dv2}')
print(f'DVs = {dv1} {dv2}')'''
