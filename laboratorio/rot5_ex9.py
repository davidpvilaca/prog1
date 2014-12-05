# DAVID VILAÇA
# 03/11/2014
# EXERCÍCIO 9

def f_ordenar (l1,l2):
	#variaveis locais
	tam = 0; i = 0; lista = []; troca = True; j = 0;
	j = len(l1)-1
	#processamento
	while j >= 0:
		lista.append(l1[j])
		j -= 1
	j = len(l2)-1
	while j >= 0:
		lista.append(l2[j])
		j -= 1
		
	tam = len(lista)
	
	while troca:
		troca = False
		for i in range(tam-1):
			if lista[i] > lista[i+1]:
				lista[i],lista[i+1] = lista[i+1], lista[i]
				troca = True
			#--fim if--
		#--fim for--
	#--fim while--
	
	return(lista)
#--fim f_ordenar--

def main():
	#variaveis
	ordenada = []
	ordem1 = [1,3,5,7,9]; ordem2 = [2,4,6,8]; #defini as listas para fazer rapido
	
	#ordenar
	ordenada = f_ordenar(ordem1,ordem2)
	
	#print
	print(ordenada)
	
	return 0
#--fim main--

if __name__ == '__main__':
	main()
#--fim if--
