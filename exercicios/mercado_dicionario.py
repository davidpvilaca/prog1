__author__ = 'David'

def cls():
    print(
        '\n'*100
    )
#-

def f_cadastraProdutos(p):

    nome = input("Digite o nome do produto a ser cadastrado ou enter para sair: ")
    while nome != "":

        if nome.lower() not in p:
            p[nome.lower()] = [int(input("Digite a quantidade no estoque: ")),0,float(input("Digite o preco: ")),[]] # array[0] = qtd estoque; [1] = vendas; [2] = preco; [3] = estoque antes de alguma atualizacao
        else:
            print("Produto já cadastrado!!!")

        nome = input("\n\nDigite o nome do produto a ser cadastrado ou enter para sair: ")
#-

def f_atualizaProdutos(p):

    nome = input("Digite o nome do produto a ser atualizado ou enter para sair: ")
    while nome.lower() != "":
        if nome.lower() not in p:
            print("Produto não cadastrado!!!")
        else:
            estoque = int(input("Estoque atual: %d mudar para: " %(p[nome.lower()][0]-p[nome.lower()][1])))
            preco = float(input("Preco atual: %.2f mudar para: " %(p[nome.lower()][2])))
            p[nome.lower()][3].append([p[nome.lower()][0],p[nome.lower()][2],p[nome.lower()][1]])
            p[nome.lower()] = [estoque,0,preco,p[nome.lower()][3]]
        
        nome = input("\n\nDigite o nome do produto a ser atualizado ou enter para sair: ")

#-

def f_vendeProdutos(p):

    nome = input("Digite o nome do produto a ser vendido ou enter para encerrar: ")
    while nome != "":
        if nome.lower() not in p:
            print("Produto não cadastrado!!!")
        else:
            preco = p[nome.lower()][2]
            qtd = int(input("Digite a quantidade a ser vendido: "))
            if qtd > p[nome.lower()][0]-p[nome.lower()][1]:
                print("ERRO! A quantidade informada excede o estoque atual!")
            else:
                p[nome.lower()][1] += qtd
                print("Venda concretizada! (R$%.2f)" %(qtd*preco))

        nome = input("\nDigite o nome do produto a ser vendido ou enter para encerrar: ")
#-

def main():

    produtos = {}

    print("FUNCOES:\n1 - Cadastrar produtos no estoque\n2 - Atualizar\Excluir estoque\n3 - Vender produtos\n\n")
    func = int(input("Digite uma funcao: "))
    while func >= 1 and func <= 3:
        if func == 1:
            print()
            f_cadastraProdutos(produtos)
        elif func == 2:
            print()
            f_atualizaProdutos(produtos)
        else:
            f_vendeProdutos(produtos)
        cls()
        print("FUNCOES:\n1 - Cadastrar produtos no estoque\n2 - Atualizar\Excluir estoque\n3 - Vender produtos\n\n")
        func = int(input("\n\nDigite uma funcao: "))
if __name__ == "__main__":
    main()
    print("Autor: %s"%(__author__))
