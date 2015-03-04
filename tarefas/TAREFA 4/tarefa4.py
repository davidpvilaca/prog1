# 16.02.2015
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

	print("PRODUTO JÁ CADASTRADO!")
	while nome != "":
		if nome in p:
			pass
		else:
			valor = float(input("Informe o valor do produto %s: " % (nome)))
			p[nome] = valor
		nome = input("\n\nInforme o nome do produto a ser cadastrado ou enter para encerrar: ")
		nome = nome.lower()


'''
Cadastro de clientes recebe como parametro um dicionario, vazio ou nao.
Sem retorno, apenas altera o dicionario
'''


def f_cadastraClientes(c):
	cpf = ""
	print("\n\nCADASTRAR CLIENTES")
	cpf = input("Digite o cpf do cliente a ser cadastrado ou enter para encerrar: ")
	while cpf != "":
		c[cpf] = []
		c[cpf].append(input("Digite o nome do cliente: "))
		c[cpf].append(input("Digite o endereco do cliente: "))
		cpf = input("\n\nDigite o cpf do cliente a ser cadastrado ou enter para encerrar: ")


'''
Cadastro de lance recebe como parametro um dicionario, vazio ou nao.
Sem retorno, apenas altera o dicionario
'''

def f_relatorio(l,c):
	maior = 0.0
	tupla = ()
	impresso = []

	print("\n--------RELATORIO--------\n")

	for keys in l:
		maior = maiorLance(l,keys[0])
		if (maior > 0) and (l[keys] == maior): #and (keys[0] not in impresso):
			print("Produto: %s  |  Valor do Lance: R$%.2f  |  CPF: %s  |  Nome do cliente: %s" %(keys[0],maior,keys[1],c[keys[1]][0]))
			#impresso.append(keys[0])


def maiorLance(l,nomeProduto):
	maior = 0
	for lk in l:
		if lk[0] == nomeProduto:
			if l[lk] > maior:
				maior = l[lk]

	return maior


def f_cadastraLance(l, p, c):
	cpf, produto, valor = "", "", 0.0
	lkProdutos, lkLances, i, j = list(p.keys()), list(l.keys()), "", 0.0
	minMax = 0.0

	cpf = input("\nPara dar um lance informe o cpf: ")
	while cpf != "":

		if cpf not in c:
			print("CPF nao cadastrado!")
		else:
			lkProdutos, lkLances = list(p.keys()), list(l.keys())
			for i in lkProdutos:
				minMax = p[i]
				for j in lkLances:
					if i in j:
						if minMax < l[j]:
							minMax = l[j]
				print(i, "R$ %.2f" % (minMax))
			#-

			produto = input("Digite o nome do produto para cadastrar o lance: ").lower()
			if produto not in p:
				print("Produto nao cadastrado!")
			else:
				minMax = p[produto]
				for j in lkLances:
					if produto in j:
						if minMax < l[j]:
							minMax = l[j]
				valor = float(input("Digite o valor do lance: "))
				if valor > minMax:
					l[(produto, cpf)] = valor
					print("Lance cadastrado com sucesso!\n\n")
				else:
					print(
						"O valo tem que ser maior que o valor minimo para lance ou maior que o valor maximo ja lancado!\n\n")
		#-if

		cpf = input("Para dar um lance informe o cpf: ")
	#-
	lkLances = list(l.keys())
	for i in lkLances:
		for j in lkProdutos:
			if j in i:
				print("%s  CPF do maior lance: %s   Valor do lance: %.2f" % (j, i[1], l[i]))

	f_relatorio(l,c)


def main():
	#variaveis
	produtos, clientes, lances = {"item1": 12.0, "item2": 4.0, "nada": 0.0}, {"144": ["david", "ES"]}, {
	("item1", "144"): 15.00}
	func = 0

	print("LEILÃO\n\n\nOPCOES:\n1 - CADASTRAR PRODUTOS\n2 - CADASTRAR CLIENTES\n3 - CADASTRAR LANCES\n")

	func = int(input("Insira uma opcao ou 0 para encerrar: "))

	while func < 0 or func > 3:
		print("OPCAO INVALIDA!")
		func = int(input("Insira uma opcao ou 0 para encerrar: "))
	#-
	while func > 0 and func < 4:
		if func == 0:
			return 0
		elif func == 1:
			f_cadastraProdutos(produtos)
		elif func == 2:
			f_cadastraClientes(clientes)
		elif func == 3:
			f_cadastraLance(lances, produtos, clientes)
		print()
		print("\n\n\n\nOPCOES:\n1 - CADASTRAR PRODUTOS\n2 - CADASTRAR CLIENTES\n3 - CADASTRAR LANCES\n")
		func = int(input("Insira uma opcao ou 0 para encerrar: "))
		while func < 0 or func > 3:
			print("OPCAO INVALIDA!")
			func = int(input("Insira uma opcao ou 0 para encerrar: "))

	return 0


if __name__ == '__main__':
	main()

