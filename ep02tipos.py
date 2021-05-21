# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------
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
