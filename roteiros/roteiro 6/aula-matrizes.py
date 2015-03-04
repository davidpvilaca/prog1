#	lista de listas 
#	
#	EXERCICIO: CRIAR FUNÇÃO QUE CRIA MATRIZES: f_criaMatriz(linhas, colunas, valor)


def iniciodaaula():
	
	matriz1 = [["a", "b","c"],["1","2","3"],["#","%%","&"],["x","xx","xxx"]]
	print(matriz1)
	print()
	print(matriz1[0][0]) #acessando dados
	
	return 0


def meio():
	#exemplo criar uma matriz com mxn
	
	m = int(input("Informe a qtd de linhas: "))
	n = int(input("Informe a qtd de colunas: "))
	
	mat = []
	
	for i in range(m):
		mat.append([])
		
	for j in range(n):
		mat[i].append(0)
	
	print(mat)
	
	return 0

meio()
