# DAVID VILAÇA
# 10.12.2014
# EXERCÍCIO 6

__author__ = 'David_Tadeu'


def f_repetidos(lista):
	#variaveis locais
	repetidos = []; i =0; tam = 0; j = 0; k = 0;
	tam = len(lista)
	
	#processamento
	for i in range(tam):
		
		for j in range(i+1,tam):
			
			if lista[i] == lista[j]:
				
				if lista[i] not in repetidos: #se o elemento da lista nao tiver ainda na lista repetidos
					repetidos.append(lista[i])
				#--fim if--
			#--fim if--
		#--fim for--
	#--fim for--
  
	return (repetidos)
#--fim f_repetidos--

def main():
	#variaveis
	l = []; repetidos = [];
	#entrada de dados
	l = [1,2,3,4,1,5,3,11,1,3,7,8,9]
	
	#verificando e obtendo repetidos
	repetidos = f_repetidos(l)
	
	#saida de dados
	print('Os elementos repetidos sao:\n')
	
	print(repetidos, end='\n\n')
	
	return 0

if __name__ == '__main__':
	main()
