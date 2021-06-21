#------------------------------------------------------------------
# Constantes que você pode utilizar nesse exercício
# Em notação científica 1.0e-6 é o o mesmo qoe 0.000001 (10 elevado a -6)
EPSILON  = 1.0e-6

#------------------------------------------------------------------
# O import abaixo permite que o programa utilize todas as funções do módulo math,
# como por exemplo, math.exp e  math.sin.
import math

#------------------------------------------------------------------
def main():
    '''() -> None

    Modifique essa função, escrevendo outros testes.
    '''
    # escolha a função que desejar e atribuia a f_x
    f_x = math.cos 
    # f_x = math.sin 
    # f_x = math.exp # etc, para integração com outras funções.
    # f_x = identidade     # identidade() definidas mais adiante
    # f_x = circunferencia # circunferencia() definida mais adiante
    # f_x = exp            # exp() definida mais adiante
 
    print("Início dos testes.")
    # Testes da f_x
    nome = f_x.__name__ # nome da f_x usada
    print(f"A função f_x usada nos testes é {nome}()")
    print(f"Valor de f_x(0.0)= {f_x( 0.0 )}")
    print(f"Valor de f_x(0.5)= {f_x( 0.5 )}")
    print(f"Valor de f_x(1.0)= {f_x( 1.0 )}")

    # testes da função área_por_retangulos
    print()
    print("Área por retângulos:")
    a, b = 0, 1 # intervalo [a,b]
    k = 1       # número de retângulos
    n = 3       # número de iterações
    i = 0
    while i < n:    
        print(f"teste {i+1}: para {k} retângulos no intervalo [{a}, {b}]:")
        print(f"    área aproximada = {area_por_retangulos(f_x, a, b, k):g}")
        k *= 10 
        i += 1

    # testes da função área_aproximada
    print()
    print("Área aproximada:")
    a, b = 0, 1 # intervalo
    k, area = area_aproximada(f_x, a, b) # número de retângulos e aproximação
    print(f"teste 1: para eps = {EPSILON:g} e intervalo [{a}, {b}]:")
    print(f"     com {k} retângulo a área é aproximadamente = {area:g}")
    eps = 1e-6 # erro relativo aceitável
    i = 1 
    n = 4
    while i < n: 
        eps *= 10 # aumenta o erro relativo aceitável
        k, area = area_aproximada(f_x, a, b, eps)
        print(f"teste {i+1}: para eps = {eps:g} e intervalo [{a}, {b}]:")
        print(f"     com {k} retângulos a área é aproximadamente = {area:g}")
        i += 1
 
    print("Fim dos testes.")
    
#------------------------------------------------------------------
# FUNÇÃO AUXILIAR PARA TESTE: função f(x)=x
def identidade( x ):
    ''' (float) -> float

    RECEBE um valor x.
    RETORNA o valor recebido. 
    EXEMPLOS:
    In [6]: identidade(3.14)
    Out[6]: 3.14
    In [7]: identidade(1)
    Out[7]: 1
    In [8]: identidade(-3)
    Out[8]: -3
    '''
    return x

#------------------------------------------------------------------
# FUNÇÃO AUXILIAR PARA TESTE: função f(x)=sqrt(1 - x*x)
def circunferencia( x ):
    ''' (float) -> float

    RECEBE um valor x.
    RETORNA um valor y >= 0 tal que (x,y) é um ponto na circunferência de raio 1 e centro (0,0).  
    PRÉ-CONDIÇÃO: a função supõe que x é um valor tal que -1 <= x <= 1.
    EXEMPLOS:
    In [9]: circunferencia(-1)
    Out[9]: 0.0
    In [10]: circunferencia(0)
    Out[10]: 1.0
    In [11]: circunferencia(1)
    Out[11]: 0.0       
    '''
    y = math.sqrt( 1 - x*x )    
    return y
#------------------------------------------------------------------
# FUNÇÃO AUXILIAR PARA TESTE: função f(x) = e^x
def exp( x ):
    ''' (float) -> float 
    RECEBE um valor x.
    RETORNA (uma aproximação de) exp(x).
    EXEMPLOS:
    In [12]: exp(1)
    Out[12]: 2.718281828459045
    In [13]: exp(0)
    Out[13]: 1.0
    In [14]: exp(-1)
    Out[14]: 0.36787944117144233
    '''
    y = math.exp( x )
    return y # return math.exp( x ) 

#------------------------------------------------------------------
#
def erro_rel(y, x):
    ''' (float, float) -> float

    RECEBE dois números x e y.
    RETORNA o erro relativo entre eles.
    EXEMPLOS:
    In  [1]: erro_rel(0, 0)
    Out [1]: 0.0
    In  [2]: erro_rel(0.01, 0)
    Out [2]: 1.0
    In  [3]: erro_rel(1.01, 1.0)
    Out [3]: 0.01
    '''
    if x == 0 and y == 0:
        return 0.0
    elif x == 0:
        return 1.0
    erro = (y-x)/x
    if erro < 0:
        return -erro
    return erro

#------------------------------------------------------------------
def area_por_retangulos(f, a, b, k):
    '''(function, float, float, int) -> float

    RECEBE uma função f, dois números a e b e um inteiro k.
    RETORNA uma aproximação da área sob a função f no intervalo [a,b] 
        usando k retângulos.
    PRÉ-CONDIÇÃO: a função supõe que a função f é continua no intervalo [a,b] e que 
         f(x) >= 0 para todo x, a <= x <= b.
    EXEMPLOS:
    In [15]area_por_retangulos(identidade, 0, 1, 1)
    Out[15]: 0.5
    In [16]:area_por_retangulos(circunferencia, -1, 0, 1)
    Out[16]: 0.8660254037844386            
    '''
    # escreva a sua solução a seguir
    base = (b-a)/k
    area = 0
    while a < b-EPSILON:
        xmeio = a+(base/2)
        altura = f(xmeio)
        area += base*altura
        a += base
    return area # aproximação

#------------------------------------------------------------------
def area_aproximada(f, a, b, eps=EPSILON):
    '''(function, float, float, float) -> int, float

    RECEBE uma função f, dois números a, b, eps.
    RETORNA um inteiro k e uma aproximação da área sob a função f no intervalo [a,b] 
        usando k retângulo.

    O valor de k deve ser a __menor potência__ de 2 tal que o erro relativo 
    da aproximação retornada seja menor que eps.

    Assim, os possíveis valores de k são 1, 2, 4, 8, 16, 32, 64, ...

    PRÉ-CONDIÇÃO: a função supõe que a função f é continua no intervalo [a,b] e que 
         f(x) >= 0 para todo x, a <= x <= b.
         
    EXEMPLOS:
    In [22]: area_aproximada(identidade, 1, 2)
    Out[22]: (2, 1.5)

    In [23]: area_aproximada(exp, 1, 2, 16)
    Out[23]: (2, 4.6224728167337865)  
    '''
    # escreva o corpo da função
    k = 1
    k1 = 1
    f_em_k = 1
    f_em_k1 = 2
    while erro_rel(f_em_k, f_em_k1) >= eps:
        k *= 2
        f_em_k = area_por_retangulos(f, a, b, k)
        f_em_k1 = area_por_retangulos(f, a, b, k1)
        k1 *= 2
    return k, area_por_retangulos(f, a, b, k)  # para retornar um int e um float 
                   # basta separá-los por vírgula 

#######################################################
###                 FIM                             ###
#######################################################
# 
#  NÃO MODIFIQUE AS LINHAS ABAIXO
# 
# Esse if serve para executar a função main() apenas quando
# este é o módulo a partir do qual a execução foi iniciada.
if __name__ == '__main__':
    main()
