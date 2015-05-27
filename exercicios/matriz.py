

def f_criaMatIdentidade(dic):
    li, col = dic[(0,0)][0],dic[(0,0)][1]

    for i in range(1,li+1):
        for j in range(1,col+1):
            if i == j:
                dic[(i,j)] = 1

    return dic



def f_imprimeMatriz(dic):
    li = dic[(0,0)][0]
    col = dic[(0,0)][1]

    for i in range(1,li+1):
        for j in range(1,col+1):
            print(dic[(li,col)],end=" ")
            print("")


    def f_criaMatriz(dic,i,j):
        li, col = 0,0
        x = 0
        dic[(0,0)] = (i,j)
        for li in range(1,i+1):
            for col in range(1,j+1):
                dic[(li,col)] = x

        return dic


    def main ():
        dic = {}
        i, j = 3,4

        dic = f_criaMatriz(dic,i,j)
        ide = f_criaMatIdentidade(dic)
        f_imprimeMatriz(ide)

        return 0

    if __name__ == "__main__":
        main()
