__author__ = 'david'

def minVal(plst):

    menor = min(plst)
    indice = plst.index(menor)

    return menor,indice
#-

def intercala(plstListas):
    lstMerge = []
    inf = 0
    limite = 0

    for i in range(len(plstListas)):
        inf += plstListas[i][-1]
    #
    for lst in plstListas:
        lst.append(inf)
        limite += len(lst)-1
    #-

    lstPos = [0]*len(plstListas)

    while len(lstMerge) < limite:
        lstAux = []
        for i in range(len(plstListas)):
            lstAux.append(plstListas[i][lstPos[i]])
        #-

        menor,index = minVal(lstAux)

        lstMerge.append(menor)
        lstPos[index] += 1
    #-
    return lstMerge
#-


def main():

    a = [[1,3,5,7,9],[2,4,6,8],[9,10,15],[11,12,13,14]]
    print(intercala(a))

    return 0

if __name__ == '__main__':
    main()
