#	
#	DAVID VILACA
#	TAREFA 4
#	
#	LEILÃO
#	

__author__ = 'David Vilaca'

'''
Cadastro de produtos recebe como parametro um dicionario, vazio ou nao.
Nao retorna, apenas altera o dicionario.
'''
def f_cadastraProdutos(p):
	nome, valor = "", 0.0
	
	nome = input("Informe o nome do produto a ser cadastrado ou enter para encerrar: ")
	nome = nome.lower()
	
	while nome != "":
		if nome in p:
			print("PRODUTO JÁ CADASTRADO!")
		else:
			valor = float(input("Informe o valor do produto %s: " %(nome)))
			p[nome] = valor
	

def main():
	
	#variaveis
	produtos, clientes, lances = {}, {}, {}
	func = 0
	
	print("LEILÃO\n\n\nOPCOES:\n1 - CADASTRAR PRODUTOS\n2 - CADASTRAR CLIENTES\n3 - CADASTRAR LANCES\n")
	
	func = int(input("Insira uma opcao ou 0 para encerrar: "))
	
	while func < 0 or func > 4:
		print("OPCAO INVALIDA!")
		func = int(input("Insira uma opcao ou 0 para encerrar: "))
	#-
	
	if func == 1:
		f_cadastraProdutos(produtos)
		
	
	return 0

if __name__ == '__main__':
	main()

