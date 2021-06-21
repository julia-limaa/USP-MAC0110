# Escreva seu programa a seguir
# Pitagoreanos = a + b + (a*a + b*b)**(1/2)
n = int(input('Digite n: '))
a = 0
b = 0
c = 0
pit = 0
pitagoreano = False
while  pit < n and a < n:
    a += 1
    b = a
    while pit < n:
        b += 1
        c = (a*a + b*b)**(1/2)
        pit = a+b+c
        if pit == n:
            pitagoreano = True
            x = a
            y = b
            z = int(c)
            pit = 0
    if pit > n:
        b = 0
        c = 0
        pit = 0
if pitagoreano:
    print(f'{n} é pitagoreano ({x},{y},{z})')
else:
    print(f'{n} não é pitagoreano')


n = int(input('Digite n: '))
a = 0
b = 0
c = 0
x = 0
y = 0
z = 0
pit = 0
pitagoreano = False
while  pit < n and a < n:
    a += 1
    b = a
    while pit < n:
        b += 1
        c = (a*a + b*b)**(1/2)
        pit = a+b+c
    if pit == n:
        pitagoreano = True
        x = a
        y = b
        z = int(c)
        pit = 0
        while a < n:
            a += 1
            b = a
            c = a
            pit = a+b+c
            while pit < n:
                b += 1
                c = (a*a + b*b)**(1/2)
                pit = a+b+c
                if pit == n:
                    x = a
                    y = b
                    z = int(c)
    if pit > n:
        b = 0
        c = 0
        pit = 0
if pitagoreano:
    print(f'{n} é pitagoreano ({x},{y},{z})')
else:
    print(f'{n} não é pitagoreano')

