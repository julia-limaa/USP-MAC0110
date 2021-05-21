#Cálculo dígito verificador
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

#Com prints
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
