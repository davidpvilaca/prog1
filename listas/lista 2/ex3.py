__author__ = 'David_Tadeu'

'''
F_BUSCA RECEBE COMO PARAMETRO LISTA DO TIPO LISTA(VETOR)
RETORNA INDICE DO TIPO INTEIRO (SE ACHOU INDICE = POSICAO SE NAO ACHOU INDICE = -1)
'''
def f_busca(lista,x):
    #variaveis locais
    indice = -1; tam = 0; achou = False; i = 0
    tam = len(lista)-1 #o comando len retorna para a variavel o tamanho da lista, no caso diminui 1 para usar no while

    #processamento
    while not achou and i <= tam: #enquanto achou for False e i tiver dentro do tamanho da lista (menor ou igual a variavel tam)

        if x == lista[i]: #se o parametro X equivaler ao elemento da lista na posicao i
            achou = True #se achou a variavel vai ficar True para sair do loop while
            indice = i+1 #o indice (posicao) eh contado +1 pois na linguagem humana nao falamos posicao 0 e sim comecamos da posicao 1
        #--fim if--

        i += 1 #contador para interromper o while caso nao ache
    #--fim while--


    return(indice)

def main():
    #variaveis
    l = [5,7,6,11,14,8,1,3,1,7,13,17]; x = 0; a = 0;

    x = 7 #X recebe o numero que queira procurar na lista

    #teste da funcao
    a = f_busca(l,x)

    #saida de dados
    if a == -1:
        print(a)
    elif a >= 0:
        print('O item %d foi encontrado na posicao %d' %(x,a))

    return 0
#--fim main--

if __name__ == '__main__':
    main()
#--fim if--