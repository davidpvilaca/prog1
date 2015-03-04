#	DAVID VILAÇA
#	ROTEIRO 7 - EXERCICIO 2



def main():
	
	#variaveis
	i, j ,k = 0,0,0
	d = {"nome": ["David", "Joao", "Maria", "Fulano", "Isabela"], "idade": [20, 23, 16, 77, 25], "telefone": ["999884572", "988657432", "996788765", "987876543", "993457613"]}
	
	while i <= (len(d)*len(d)):
		for j in d:
			for k in range(len(d[j])):
				if k == i:
					print(str(j)+ ": "+str(d[j][k]))
		i += 1
	
	return 0

if __name__ == '__main__':
	main()

