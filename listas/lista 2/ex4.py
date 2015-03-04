__author__ = 'David_Tadeu'


def main():
    #variaveis
    l1 = []; l2 = []; l3 = []; i = 0; aux1=0; aux2=-1;

    #entrada de dados
    for i in range(10):
        l1.append(int(input('Insira um numero para lista1: ')))
    for i in range(10):
        l2.append(int(input('Insira um numero para lista2: ')))

    #processamento
    for i in range(10): #loop com i sendo valores de 0 a 19, ou seja, ira repetir o loop 20 vezes
        if i%2 == 0: #se i for par (resto da divisao por 2 = 0)
            l3.append(l1[i]) #a lista l3 vai receber o equivalente da lista l1
        elif i%2 != 0: #se i for impar
            l3.append(l2[i]) #a lista l3 vai receber o equivalente da lista l1


    #saida de dados
    print(l3) #imprimindo l3 na tela


    return 0
#--fim main--

if __name__ == '__main__':
    main()
#--fim if--