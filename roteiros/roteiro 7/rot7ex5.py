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
	aux = []
	d = {"nome": ["David", "Joao", "Maria", "Fulano", "Isabela"], "idade": [20, 23, 16, 77, 25], "telefone": [999884572, 988657432, 996788765, 987876543, 993457613]}
	
	f_ordena(d["nome"])
	
	for i in d["nome"]:
		print("Nome: %s"%(i))
		
	return 0

if __name__ == '__main__':
	main()

