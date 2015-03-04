# faça uma função que cadastre produtos (novos).
# faça uma função para vender os produtos. Incremente a qtd
#  vendida até o limite do estoque
# faça uma função que imprima o relatorio de vendas (Ex: Macarrao R$...)

def insereProdutos(produtos):
	
	lst, nome, preco, vendasI, estoque = [],"",0.0,0,0
	
	nome = input("Insira o nome do produto: ")
	while nome != "":
		if nome in produtos:
			print("Produto já cadastrado!")
		else:
			estoque = int(input("Insira a quatidade no estoque: "))
			preco = float(input("Insira o preço: "))
			lst = [estoque, vendasI, preco]
			produtos[nome] = lst
			nome = input("Insira o nome do produto: ")

def vendeProdutos(produtos):
	
	nome, qtd = "",0
	
	nome = input("Insira o nome do produto a ser vendido: ")
	
	while nome != "":
		if nome not in produtos:
			print("Este produto não existe!")
		else:
			qtd = int(input("Quantidade: "))
			if qtd > produtos[nome][0]:
				print("A quantidade excede ao estoque!")
			else:
				produtos[nome][1] = produtos[nome][1]+qtd
		nome = input("Insira o nome do produto a ser vendido: ")
	
def relatorioVendas(produtos):
	
	print("Relatorios")
	
	nome = input("Digite o nome do produto que deseja o relatorio: ")
	
	while nome != "":
		if nome not in produtos:
			print("Produto não cadastrado!")
		else:
			estoque = produtos[nome][0]
			qtdVendas = produtos[nome][1]
			preco = produtos[nome][2]
			
			print("O produto %s foi vendido %d  vezes por R$%.2f\n\nTotal em reais vendido: R$%.2f\n\nAinda restam %d no estoque." %(nome,qtdVendas,preco,preco*qtdVendas,estoque-qtdVendas))
		nome = input("\n\nDigite o nome do produto que deseja o relatorio: ")
	

def main():
	#var
	produtos = {}
	
	insereProdutos(produtos)
	vendeProdutos(produtos)
	relatorioVendas(produtos)
	
	return 0
	
if __name__ == "__main__":
	main()
