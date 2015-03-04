__author__ = 'David_Tadeu'
__date__ = '12.12.14'

'''
F_SUBTRACAO ENTRA COM L1 E L2 (LISTAS)
RETORNA LISTA (LISTA) QUE EH O RESULTADO DE L1-L2
'''
def f_subtracao(l1, l2):
    # variaveis locais
    i = 0
    j = 0
    taml1 = 0
    taml2 = 0
    lista = []


    taml1 = len(l1)
    taml2 = len(l2)

    # processamento
    if taml1 >= taml2:
        for i in range(taml1):
            if i < taml2:
                lista.append(l1[i]-l2[i])
            elif taml2 <= i:
                lista.append(l1[i])
            # --fim if--
        # --fim for--

    elif taml2 > taml1:
        for i in range(taml2):
            if i < taml1:
                lista.append(l1[i]-l2[i])
            elif taml1 <= i:
                lista.append(-l2[i])
            # --fi if--
        # --fim for--
    # --fim if--



    return(lista)
# --fim f_subtracao--

def main():
    # variaveis
    l1 = []
    l2 = []
    l3 = []

    # entrada de dados
    l1 = [5, 4, 2, 1, 9, 5, 2]
    l2 = [1, 2, 3, 4, 5, 6, 2, 3, 1]

    # subtracao
    l3 = f_subtracao(l1,l2)

    print(l3)

    return 0

# --fim main--

if __name__ == '__main__':
    main()
    #--fim if--