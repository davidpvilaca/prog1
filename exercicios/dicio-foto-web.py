__author__ = 'david'
#09-03-2015





'''
Funcao que insere figuras(string) num dicionario atraves da chave nome
'''
def f_insereFiguras(dic,nome,x1,y1,x2,y2):

    if nome in dic:
        print("Foto já cadastrada!")
    #else:


#- fim cadastraFiguras


def f_sobrepoe(d,x1,y1,x2,y2):

    x, y = 0,0

    for i in d:
        if (d[i][0] < x1 < d[i][2]) or (d[i][1] < y1 < d[i][3]) or (d[i][0] < x2 < d[i][2]) or (d[i][1] < y2 < d[i][3]):
            return True
        else:
            return False


def f_cadastraPropaganda(d):

    x1,y1,x2,y2, nome, display = 0,0,0,0,"",(1024,768)

    nome = input("Digite o nome da imagem ou enter para encerrar: ")

    while nome != "":

        if nome not in d:
            x1 = int(input("Informe a posicao inicial no display (Largura): "))
            y1 = int(input("Informe a posicao inicial no display (Altura): "))
            x2 = int(input("Informe a posicao final no display (Largura): "))
            y2 = int(input("Informe a posicao final no display (Altura): "))

            if f_sobrepoe(d,x1,y1,x2,y2):
                print("Esta sobrepondo por favor reinicie o cadastramento!\n")
            #else:


        else:
            print("Produto já cadastrado!")



        nome = input("Digite o nome da imagem ou enter para encerrar: ")


def main():
    #var
    dic = {}; x1,y1,x2,y2 = 0,0,0,0

    dic = {"Gato.jpg": [100,10,200,110,10]}

    print(f_sobrepoe(dic,900,60,1024,768))

    return 0

if __name__ == '__main__':
    main()
