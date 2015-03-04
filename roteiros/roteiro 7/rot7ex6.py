#	DAVID VILAÇA
#	ROTEIRO 7 - EXERCICIO 5

def f_ordena(lista):

	#variaveis locias
	i = 0; aux = 0; trocas = 0;
	lenl = 0

	#processamento
	lenl = len(lista)
	trocas = 1

	while trocas != 0:
		trocas = 0
		for i in range(lenl-1):
			if lista[i] > lista[(i+1)]:
				aux = lista[i]
				lista[i] = lista[(i+1)]
				lista[(i+1)] = aux
				trocas += 1

		#--fim if--
	#--fim for--

#--fim f_ordena--

def main():
	
	#variaveis
	acaba = False
	i = ""
	j = 0
	aux = []; maiores = {"nome": [], "telefone": [], "idade": []}
	d = {"nome": ["David", "Joao", "Maria", "Fulano", "Isabela"], "idade": [20, 15, 16, 77, 25], "telefone": [999884572, 988657432, 996788765, 987876543, 993457613]}

	f_ordena(d["nome"])
	menores = {"nome": [], "telefone": [], "idade": []}
	aux = list(maiores.keys())
	
	for i in range(len(d["nome"])):
		aux = list(maiores.keys())
		if d["idade"][i] >= 18:
			if len(aux) == 0:
				maiores["nome"] = [d["nome"][i]]
				maiores["idade"] = [d["idade"][i]]
				maiores["telefone"] = [d["telefone"][i]]
			else:
				maiores["nome"].append(d["nome"][i])
				maiores["idade"].append(d["idade"][i])
				maiores["telefone"].append(d["telefone"][i])
		else:
			if len(aux) == 0:
				menores["idade"] = [d["idade"][i]]
				menores["nome"] = [d["nome"][i]]
				menores["telefone"] = [d["telefone"][i]]
			else:
				menores["idade"].append(d["idade"][i])
				menores["nome"].append(d["nome"][i])
				menores["telefone"].append(d["telefone"][i])

	d = menores

	print(maiores)
	print (d)

	return 0

if __name__ == '__main__':
	main()

