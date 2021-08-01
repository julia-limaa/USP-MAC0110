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
# Constantes
# use essas constantes caso desejar

DNA = 'ATCG'
GAP = '_'


#------------------------------------------------------------------
def main():
    '''
        Modifique essa função, escrevendo os seus testes.
    '''
    print("main(): início dos teste")
    ## Escreva aqui os testes para a função gera_gaps
    print(gera_gaps('T'))
    ## Escreva aqui os testes para a função pontuação
    print(pontuacao('T_CGTA','A_CGT_',-1,5,3,2))
    print(pontuacao('__T_CG', '_AT_CG', 5, 4, 3, 2))
    #  Comece por exemplo escrevendo os exemplos mostrados 
    #  nesse arquivo, na especificação de cada função.       
    print("main(): fim dos testes")


#------------------------------------------------------------------
#
def gera_gaps( dna ):
    ''' ( str ) -> list

    RECEBE uma string `dna` representando uma fita de DNA com os
    símbolos 'A', 'T', 'C', 'G' e '_' (GAP).

    RETORNA uma lista com todas as variações de dna com um símbolo GAP 
    a mais e sem repetições.

    exemplos: 
    In  [1]: gera_gaps( 'T' )
    Out [1]: ['_T', 'T_']
    
    In  [2]: gera_gaps( 'CA' )
    Out [2]: ['_CA', 'C_A', 'CA_']
    
    In  [3]: gera_gaps( 'AT_G')
    Out [3]: ['_AT_G', 'A_T_G', 'AT__G', 'AT_G_'] 
    '''
    # modifique o código abaixo para conter a sua solução.
    com_gap = [] 
    for i in range(len(dna)+1):
        gap = dna[:i]+'_'+dna[i:]
        if gap != (dna[:i-1]+'_'+dna[i-1:]) or (i == 0):
            com_gap += [gap]
    return com_gap

#------------------------------------------------------------------
#
def pontuacao(s, t, ga, la, ldif, lgap):
    ''' (str, str, int, int, int, int) -> int

    RECEBE duas strings `s` e `t` de mesmo tamanho com zero ou mais gaps 
    representando fitas de DNA; e quatro inteiros `ga`, `la`, `ldif`, `lgap`.
 
    RETORNA a pontuação do alinhamento entre `s` e `t` calculada da seguinte 
    forma:

       * dois gaps alinhados contam `ga` pontos,
       * duas letras iguais alinhadas contam `la` pontos, 
       * duas letras diferentes alinhadas contam `-ldif` pontos (subtrai ldif pontos) e 
       * uma letra alinhada com um gap contam `-lgap` pontos (subtrai lgap pontos).

    Exemplos:

    In  [1]: pontuacao('T_', 'CT', 1, 5, 6, 3)
    Out [1]: -9

    In  [2]: pontuacao('T_CGTAC', 'T_CG_TC', 1, 5, 6, 3)
    Out [2]: 12
    
    In  [3]: pontuacao('T_CGTAC', 'A_CG_T_', 2, 3, 5, 4)
    Out [3]: -10
    
    In  [4]: pontuacao('T_CGTA',  'A_CGT_', -1, 5, 3, 2)
    Out [4]: 9
    '''
    # modifique o código abaixo para conter a sua solução.
    pontos = 0
    for i in range(len(s)):
        if s[i] == t[i]:
            if s[i] == '_':
                pontos += ga
            else:
                pontos += la
        else:
            if s[i] != '_' and t[i] != '_':
                pontos -= ldif
            else:
                pontos -= lgap
    return pontos
    

#######################################################
###                 FIM                             ###
#######################################################
# 
# Esse if serve para rodar a main() dentro do Spyder.

if __name__ == '__main__':
    main()
