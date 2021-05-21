# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------
     
'''
    Nome: colocar no tipos.py, nome oficial
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

s = str(input('Digite uma string s: '))
i = int(input('Digite um inteiro i: '))
x = float(input('Digite um float x: '))
print(('s = 'f"'{s}'"), f'({type(s)})')
print(('i = 'f'{i}'), f'({type(i)})') 
print(('x = 'f'{x}'), f'({type(x)})')
print((('s + s = 'f"'{s}' + '{s}' = "f"'{s+s}'")), f'({type(s+s)})')
print((('i + i = 'f"{i} + {i} = "f'{i+i}')), f'({type(i+i)})')
print((('x + x = 'f"{x} + {x} = "f'{x+x}')), f'({type(x+x)})')
print((('i * s = 'f"{i} * '{s}' = "f"'{i*s}'")), f'({type(i*s)})')
print((('i * i = 'f"{i} * {i} = "f'{i*i}')), f'({type(i*i)})')
print((('i * x = 'f"{i} * {x} = "f'{i*x}')), f'({type(i*x)})')
print((('x / i = 'f"{x} / {i} = "f'{x/i}')), f'({type(x/i)})')
print((('i / i = 'f"{i} / {i} = "f'{i/i}')), f'({type(i/i)})')
print((('i // i = 'f"{i} // {i} = "f'{i//i}')), f'({type(i//i)})')
print((('i / 2 * 3 = 'f"{i} / 2 * 3 = "f'{i/2*3}')), f'({type(i/2*3)})')
print((('i // 2 * 3 = 'f"{i} // 2 * 3 = "f'{i//2*3}')), f'({type(i//2*3)})')
print((('i % 3 = 'f"{i} % 3 = "f'{i%3}')), f'({type(i%3)})')