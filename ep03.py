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
