#	DAVID VILAÇA
#	ROTEIRO 7 - EXERCICIO 3



def main():
	
	#variaveis
	aux = []
	d = {"1nome": ["David", "Joao", "Maria", "Fulano", "Isabela"], "2idade": [20, 23, 16, 77, 25], "3telefone": ["999884572", "988657432", "996788765", "987876543", "993457613"]}
	aux = list(d.keys())
	aux.sort()
	
	for i in range(len(d["1nome"])):
		for j in aux:
			print(d[j][i])
	
			
	
	
	return 0

if __name__ == '__main__':
	main()

