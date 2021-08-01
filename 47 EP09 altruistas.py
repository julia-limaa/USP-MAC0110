# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
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
#####################################################################
# MÓDULOS A SEREM UTILIZADOS NO PROGRAMA
# random.shuffle()
import random

# time.time()
import time 

#-----------------------------------------------------------------------
def main():
    '''(None) -> None

    Unidade de teste para as funções pedidas no EP.
    Escreva outros testes que desejar.
    '''
    print("Início dos testes")

    # testes da função no_egoistas()
    print()
    print("Teste no_egoistas()")
    amigos1 = [1,2,3,4,0]
    amigos2 = [2,1,0,3,4]
    print(f"    no_egoistas({amigos1}) = {no_egoistas(amigos1)}")
    print(f"    no_egoistas({amigos2}) = {no_egoistas(amigos2)}")

    # para efeito de reprodutibilidade dos experimentos
    semente = int(input("Digite o valor da semente do gerador de números pseudo-aleatórios: "))
    random.seed(semente)

    # parâmetros para os experimentos
    print("\nParâmetros para o experimento ")
    ini    = int(input("Digite o número mínimo de pessoas: "))
    fim    = int(input("Digite o número máximo de pessoas: "))
    passo  = int(input("Digite o passo: "))
    T      = int(input("Digite o número de tentativas em cada experimento: "))
    mostre = input("Deseja ver as listas com índices egoistas [s/n]: ")

    print("\nTeste experimento()")
    # estima q(N) para vários valores de N
    for N in range(ini, fim, passo):
        # inicie o cronômetro
        t_ini = time.time()
        # execute o experimento
        qN, lst_egoistas = experimento(N, T)
        # exiba a estimativa do valor de q(N)
        print(f"q({N}) = {qN}")
        if mostre in ['s', 'S']: 
            print(f"    lista com índices egoistas para q({N}): ")
            tamanho = len(lst_egoistas)
            if tamanho == 0:
                print("      nenhuma lista possui índice egoísta")
            else:
            # transforme listas com egoistas em listas sem 
                for i in range(0, tamanho, 1):
                    print(f"    antes : {lst_egoistas[i]}")
                    altruistas(lst_egoistas[i])
                    print(f"    depois: {lst_egoistas[i]}")
    # pare cronômetro            
        t_fim = time.time()
        print(f"    tempo decorrido: {(t_fim - t_ini)*1000:7.2f} ms")

    # teste altruismo() n grande
    print("\nTeste altruismo() para lista grande")
    muito_grande = 1000000
    amigos3  = sorteie_amigos(muito_grande)
    amigos3 += [muito_grande] # garante índice egoísta
    print(f"    no. de egoístas com lista de {muito_grande} = {no_egoistas(amigos3)}")
    t_ini = time.time() # inicie o cronômetro
    altruistas(amigos3)
    t_fim = time.time() # pare cronômetro 
    print(f"    no. de egoístas com lista de {muito_grande} = {no_egoistas(amigos3)}")
    print(f"    tempo decorrido: {(t_fim - t_ini)*1000:7.2f} ms")

    print("\nFim dos testes")

#-----------------------------------------------------------------------
def sorteie_amigos(N):
    ''' (int) -> list
    RECEBE um inteiro N > 0.
    RETORNA uma lista de tamanho N, contendo os números de 0 a N em 
        ordem aleatória.

    ATENÇÃO: a tabulação das linhas foi removida e a ordem de algumas 
    linhas alterada. Ela deve ser consertada antes possa ser utilizada.
    '''
    i = 0
    amigos = []
    while i < N:
        amigos += [i]
        i += 1
    random.shuffle(amigos)
    return amigos
        
#-----------------------------------------------------------------------
def no_egoistas(amigo_de):
    '''(list) -> int

    RECEBE uma lista amigo_de.
    RETORNA o número de indices egoistas na lista.
    '''
    # modifique o código abaixo para conter a sua solução. [2,1,0,3,4]
    egoistas = 0
    for i in range (len(amigo_de)):
        if amigo_de[i] == i:
            egoistas += 1
    return egoistas

#-----------------------------------------------------------------------
def experimento(N, T):
    '''(int, int) -> float, list

    RECEBE inteiros positivos N e T.

    Estima a probabilidade q(N) de uma lista de "amigo secreto" 
    com N participantes NÃO ter um índice egoista.

    A função realiza T sorteios de listas de tamanha N e utiliza 
    como estimador a razão entre o número de listas sem egoistas e T.

    RETORNA a probabilidade estimada para q(N) e uma lista formada
    por todas as listas com índices egoístas sorteadas durante 
    o experimento.
    '''
    # modifique o código abaixo para conter a sua solução.
    s = 0
    listas_egoistas = []
    for i in range (T):
        lista_aleatoria = sorteie_amigos(N)
        if no_egoistas(lista_aleatoria) != 0:
            s+= 1
            listas_egoistas += [lista_aleatoria]
        i +=1
    return (1-s/T), listas_egoistas  # retorna uma estimativa probabilidade e uma lista de listas

#-----------------------------------------------------------------------
def altruistas(amigo_de):
    ''' (list) -> None

    RECEBE uma lista amigo_de.
    REARRANJA itens da lista de tal forma que ela passe a não possuir 
        índices egoístas.
    '''
    # modifique o código abaixo para conter a sua solução.
    if no_egoistas(amigo_de) != 0:
        egoista = True
        while egoista:
            lista_altruista = sorteie_amigos(len(amigo_de))
            if no_egoistas(lista_altruista) == 0:
                amigo_de[:] = lista_altruista[:]
                egoista = False

#=====================================================================
# Não modifique as linhas abaixo
# Esse if serve para rodar a main() dentro do Spyder
# e não atrapalhar o corretor automático
if __name__ == '__main__':
    main()
