#Biblioteca David - MATRIZES

def f_criaMatriz(m,n,e):
	#var
	criada, i, j = [],0,0
	
	#processamento
	for i in range(m):
		criada.append([])	
		for j in range(n):
			criada[i].append(e)
		#-
	#-
	return criada

def f_imprimeMatriz(matriz):
	
	i, j, aux = 0,0,0
	linhas = len(matriz)
	
	for i in range(linhas):
		aux = len(matriz[i])
		for j in range(aux):
			print (matriz[i][j], end=" ")
		print()
		
def f_verificaMatriz(matriz):
	i,j = 0,0
	linhas = len(matriz)
	colunas = 0
	aux = 0
	
	while i < linhas:
		colunas = len(matriz[i])
		if i == 0:
			aux = colunas
		if colunas != aux:
			return False
			
		i += 1

def f_matrizIdentidade(n):
	
	i,j, matriz = 0,0,[]
	
	for i in range(n):
		matriz.append([])
		for j in range(n):
			if i == j:
				matriz[i].append(1)
			else:
				matriz[i].append(0)
	
	return matriz

def f_verificaIdentidade(matriz):
	i, j, linhas, colunas, aux = 0,0,0,0,0
	linhas = len(matriz)
	
	if linhas==1:
		return False
	
	for i in range(linhas):
		colunas = len(matriz[i])
		for j in range(colunas):
			if i == j:
				if matriz[i][j] == 1:
					aux += 1
	if aux == linhas:
		return True
	else:
		return False

def f_verificaQuadrada(matriz):
	i, j, aux  = 0,0,0
	linhas = len(matriz)
	for i in range(linhas):
		colunas = len(matriz[i])
		if linhas == colunas:
			aux += 1
		
	if aux == linhas:
		return True
	else:
		return False

def f_qtdZeros(matriz):
	#var
	i, j, linhas, colunas, qtd = 0,0,len(matriz),0, 0
	
	for i in range(linhas):
		colunas = len(matriz[i])
		for j in range(colunas):
			if matriz[i][j] == 0:
				qtd += 1
	return qtd

def f_somaDiag(matriz):
	#var
	i, j, linhas, colunas = 0,0,len(matriz),0
	soma = 0
	
	for i in range(linhas):
		colunas = len(matriz[i])
		for j in range(colunas):
			if i == j:
				soma += matriz[i][j]
	return soma

def f_calculaTransposta(matriz):
	i,j,linha,coluna = 0,0,len(matriz),len(matriz[0])
	
	transposta = f_criaMatriz(coluna,linha,0)
	
	for i in range(linha):
		for j in range(coluna):
			transposta[j][i] = matriz[i][j]
	
	return transposta

def f_verificaSimetrica(matriz):
	i, j, linhas, colunas, aux = 0,0,len(matriz),len(matriz[0]),0
	if linhas != colunas:
		return False
	matrizT = f_calculaTransposta(matriz)
	for i in range(linhas):
		for j in range(colunas):
			if matrizT[i][j] == matriz[i][j]:
				aux += 1
	if aux == linhas*colunas:
		return True
	else:
		return False

def f_verificaMenor(matriz):
	i,j,linhas,colunas,aux = 0,0,len(matriz),0,0
	
	for i in range(linhas):
		colunas = len(matriz[i])
		for j in range(colunas):
			if i == 0 and j == 0:
				aux = matriz[i][j]
			if matriz[i][j] < aux:
				aux = matriz[i][j]
	return aux

def f_somaLinhas(mat):
	i, j, soma, linhas, colunas, aux = 0,0,[],len(mat),0,0
	
	while i < linhas:
		colunas = len(mat[i])
		for j in range(colunas):
			aux = aux+mat[i][j]
		soma.append(aux)
		aux = 0
		
		i += 1
	
	return soma

def f_somaMatriz(m1,m2):
	i, j, aux, linhas, colunas, soma = 0,0,0,len(m1),0,[]
	
	if len(m1) != len(m2):
		return 0
	if len(m1[0]) != len(m2[0]):
		return 0
	
	for i in range(linhas):
		colunas = len(m1[i])
		soma.append([])
		for j in range(colunas):
			soma[i].append(m1[i][j]+m2[i][j])
	#-
	return soma

def f_multiplicaMatriz(m1,m2):
	mat3, linha, coluna, i,j,k, acumula = [],len(m1),len(m2[0]),0,0,0,0
	
	if len(m1[0]) != len(m2):
		print("Erro! O número de colunas da primeira matriz informada não é igual ao número de linhas da segunda!")
		return 0
	
	for i in range(linha):
		mat3.append([])
		for j in range(coluna):
			acumula = 0
			for k in range(len(m1[0])):
				acumula = acumula+m1[i][k]*m2[k][j]
			#-
			mat3[i].append(acumula)
		#-
	#-
	
	return mat3
