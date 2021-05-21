# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
# ------------------------------------------------------------------

"""
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

"""

##################################################################
## ESCREVA SEU PROGRAMA ABAIXO

x = float(input('Digite um número x entre 0 e 8: '))
y = float(input('Digite um número y entre 0 e 8: '))
local = 'azul'
sobrancelha = (x>=1 and x<=3 and y>=7.25 and y<=7.75) or (x>=5 and x<=7 and y>=7.25 and y<=7.75)
olho1 = (((x-2)*(x-2))+((y-6)*(y-6))<=1 and x>=1 and x<=3 and y>=5 and y<=7) and not (((x-2)*(x-2))+((y-6)*(y-6))<=0.25 and x>=1.5 and x<=2.5 and y>=5.5 and y<=6.5)
olho2 = (((x-6)*(x-6))+((y-6)*(y-6))<=1 and x>=5 and x<=7 and y>=5 and y<=7) and not (((x-6)*(x-6))+((y-6)*(y-6))<=0.25 and x>=5.5 and x<=6.5 and y>=5.5 and y<=6.5)
nariz = x>=3.5 and x<=4.5 and y>=3.5 and y<=4.5
boca = (((x-3)*(x-3))+((y-2)*(y-2))<=0.25 and x>2.5 and x<=3.5 and y>1.5 and y<2.5) or (x>=3 and x<=5 and y>1.5 and y<2.5) or (((x-5)*(x-5))+((y-2)*(y-2))<=0.25 and x>=4.5 and x<5.5 and y>1.5 and y<2.5)
canto1= x>=0 and x<1 and y>=0 and y<2
canto2 = x>7 and x<=8 and y>=0 and y<2
fora = x<0 or x>8 or y<0 or y>8
if sobrancelha or olho1 or olho2 or nariz or boca or canto1 or canto2 or fora:
    local = ('branco')
print(local)