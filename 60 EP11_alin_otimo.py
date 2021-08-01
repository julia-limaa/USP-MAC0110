# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS OU ATRIBUTOS
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

# módulo alinhamento: alin.gera_gaps(), alin.pontuacao()
import alinhamento as alin

# Constantes
# use essas constantes caso desejar
DNA = 'ATCG'
GAP = '_'

#------------------------------------------------------------------
def main():
    '''
        Modifique essa função, escrevendo os seus testes.
    '''

    ## exemplos de chamada da função do módulo alinhamento
    #print('Testes das funções do módulo alinhamento:')
    #print(alin.gera_gaps( 'T' ))
    #print(alin.gera_gaps( 'CA' ))
    #print(alin.gera_gaps( 'AT_G' ))

    #print(alin.pontuacao('T_', 'CT', 1, 5, 6, 3))
    #print(alin.pontuacao('T_CGTAC', 'T_CG_TC', 1, 5, 6, 3))
    #print(alin.pontuacao('T_CGTAC', 'A_CG_T_', 2, 3, 5, 4))
    #print(alin.pontuacao('T_CGTA',  'A_CGT_', -1, 5, 3, 2))
    #print()

    ## Escreva aqui os testes para a função gera_n_gaps()
    #print(gera_n_gaps( 'T', 2 ))
    #print(gera_n_gaps( 'CA', 2 ))
    #print(gera_n_gaps( 'C_A', 2))
    #print(gera_n_gaps('T_CG', 1))
    #print(gera_n_gaps('ATCG', 2))
    #print(gera_n_gaps('T', 4))
    #print(gera_n_gaps('AT_C_G_AT_CG_AATTCG_TCGA'))

    ## Escreva aqui os testes para a função pontuacao_max()
    print(pontuacao_max('T_CG', 'ATCG', 5, 4, 3, 2))
    print(pontuacao_max('T_CGTAC', 'ATCG_T_', 0, 1, 4, 3, 2))
    print(pontuacao_max('AT_', 'A_T', 2, 5, 1, 0, 2))
 
    print("Fim dos meus testes.")

#------------------------------------------------------------------
def gera_n_gaps( dna, n = 1 ):
    '''( str, int ) -> list

    RECEBE uma string `dna` representando uma fita de DNA com os
    símbolos 'A', 'T', 'C', 'G' e '_' (gap), e um número inteiro positivo `n`.
 
    RETORNA uma lista sem repetições com todas as variações de `dna` 
    com até `n` gaps extras.

    EXEMPLOS:
 
    In [1]: gera_n_gaps( 'T', 2 )
    Out[1]: ['T', '_T', 'T_', '__T', '_T_', 'T__']
    
    In [2]: gera_n_gaps( 'CA', 2 )
    Out[2]: ['CA', '_CA', 'C_A', 'CA_', '__CA', '_C_A', '_CA_', 'C__A', 'C_A_', 'CA__']
    
    In [3]: gera_n_gaps( 'C_A', 2)
    Out[3]: ['C_A', '_C_A', 'C__A', 'C_A_', '__C_A', '_C__A', '_C_A_', 'C___A', 'C__A_', 'C_A__']
    '''
    # modifique o código abaixo para conter a sua solução.
    dna_novo, elemento = dna, dna
    com_gaps = [dna] 
    gaps = conta_gaps(dna) # conta quantos gaps já tem na string "dna"

    i = 0  
    while conta_gaps(elemento) < n+gaps:
        elemento = com_gaps[i] 
        if conta_gaps(elemento) < n+gaps:
            dna_novo = alin.gera_gaps(elemento)
            for x in dna_novo:
                if x not in com_gaps:
                    com_gaps += [x]
        i += 1
        
    return com_gaps
#------------------------------------------------------------------
def conta_gaps(algo):
    gap = 0
    for k in algo:
        if k == '_':
            gap += 1
    return gap
#------------------------------------------------------------------
def pontuacao_max(s, t, ga, la, ldif, lgap, n = 1):
    '''(str, str, int, int, int, int, int) -> int, list de list

    RECEBE:

        - duas strings `s` e `t` de mesmo comprimento representando fitas de DNA 
          com os símbolos 'A', 'T', 'C', 'G' e '_' (gap); e
        - quatro números inteiros `ga`, `la`, `ldif` e `lgap` como no EP10;
        - mais um número inteiro positivo `n`.

    RETORNA 

        - a maior pontuação entre pares de variações de s e t que têm:

              * o mesmo comprimento; 
              * até `n` gaps extras.

        - uma lista com todos os pares de variações de s e t que têm 
          esta maior pontuação; cada par é uma lista com duas variações.

    Exemplos:

    In [1]: pontuacao_max('T_CG', 'ATCG', 5, 4, 3, 2)
    Out[1]: (15, [['_T_CG', 'AT_CG']])

    In [2]: pontuacao_max('T_CGTAC', 'ATCG_T_', 0, 1, 4, 3, 2)
    Out[2]: (-5, [['_T_CG_TAC', 'AT_CG_T__']])

    In [3]: pontuacao_max('AT_', 'A_T', 2, 5, 1, 0, 2)
    Out[3]: (16, [['_A_T_', '_A_T_'], 
                  ['A__T_', 'A__T_'], 
                  ['A_T__', 'A_T__']])
    '''
    # modifique o código abaixo para conter a sua solução.
    pont_max = alin.pontuacao(s,t, ga, la, ldif, lgap)
    pares = []
    
    com_gaps_s = gera_n_gaps(s, n)
    com_gaps_t = gera_n_gaps(t, n)
    
    for str_s in com_gaps_s:
        for str_t in com_gaps_t:

            if len(str_s)==len(str_t):
                pontuacao = alin.pontuacao(str_s,str_t, ga, la, ldif, lgap)

                if pontuacao > pont_max:
                    pont_max = pontuacao
                    pares = []
                    pares += [[str_s, str_t]]
                elif pontuacao == pont_max:
                    pares += [[str_s,str_t]]  

    return pont_max, pares
    

#######################################################
###                 FIM                             ###
#######################################################
# 
# Esse if serve para rodar a main() dentro do Spyder.

if __name__ == '__main__':
    main()
