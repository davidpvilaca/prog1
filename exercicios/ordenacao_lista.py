#	ORDENACAO BOLHA
#	02-12-14
#	DAVID VILACA

#########################################################
#														#
#	ORDENACAO DE LISTA ATRAVES DE UMA FUNCAO SIMPLES	#
#														#
#########################################################

__author__ = 'davidvilaca'

'''
FUNCAO DE ORDENACAO ENTRA COM VETOR (LISTA)
RETORNA NAO RETORNA POIS LISTAS SAO MUTAVEIS
'''
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
	#declaracao de variaveis
	vetor = []; aux = "";
	
	#entrada de dados
	print('######################\n# ORDENACAO DE LISTA #\n######################')
	
	aux = input('Insira um valor para lista ou digite "fim" para encerrar: ')
	
	while aux != "fim" and aux != "FIM" and aux != "Fim":
		aux = int(aux)
		vetor.append(aux)
		aux = input('Insira um valor para lista ou digite "fim" para encerrar: ')
	#--fim while--
	
	print('\nLista sem ordem:')
	print(vetor)
	
	#ordenando/chamada da funcao
	f_ordena(vetor)
	
	#saida de dados
	print ('\nLista em ordem crescente:')
	print(vetor)
	
	return 0

if __name__ == '__main__':
	main()

