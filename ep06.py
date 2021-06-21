#----------------------------------------------------    
def primo(n):
    '''(int) -> boo
    
       RECEBE um número inteiro n.
       RETORNA True se n é primo e False em caso contrário.
    ''' 
    div = 2
    prim = True
    if n <= 1:
        prim = False
    while div*div <= n and prim:
        if n % div == 0:
            prim = False
        div += 1
    return prim
#----------------------------------------------------        
def goldbach(n):
    '''(int) -> bool, int, int 

       RECEBE um número inteiro n.
       RETORNA True, p, q se n é soma de dois números primos p e q.
       Se n não é soma de dois números primos a função retorna False, 1, 1.
    '''
    p = 1
    q = 1
    i = 0
    j = 0
    gold = False
    while p < n and not gold:
        p += 1
        q = 0
        i = primo(p)
        while i and p + q < n:
            q += 1
            j = primo(q)
            if j and p+q == n:
                gold = True
                return True, p, q
    if gold == False:
        return False, 1, 1

#----------------------------------------------------    
def exponencial(n0, e, p, d):
    '''(int, int, float, int) -> int 

       RECEBE 

         * o número n0 de indivíduos infectados em um dia 0;
         * o número diário médio e de indivíduos com quem alguém 
           infectado é exposto;
         * a probabilidade p de uma exposição resultar em uma infecção;
         * um inteiro d,  d >=  0. 

      RETORNA o número total de indivíduos infectados até o dia d 
      determinado por (n0, e, p).
    '''
    n_infec = ((1 + e*p)**d) * n0
    return int(n_infec)
    
#--------------------------------------------------
def logistica(n0, e, p, n, d):
    '''(int, int, float, int, int) -> int
 
       RECEBE 

         * o número n0 de indivíduos infectados em um dia 0;
         * o número diário médio e de indivíduos com quem alguém 
           infectado é exposto;
         * a probabilidade p de uma exposição resultar em uma infecção;
         * o número n de indivíduos na população; e
         * um inteiro d, d >= 0. 

       RETORNA o número total de indivíduos infectados até o dia d 
       determinado por (n0, e, p, n).

    '''
    if d == 0:
        n_infec = n0
        return n_infec

    n_ant = n0
    d0 = 0
    while d0 < d:
        n_infec = (1 + e*p*(1-(n_ant/n))) * n_ant
        n_ant = n_infec
        d0 += 1
    return int(n_infec)
    
