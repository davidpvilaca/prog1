# DAVID VILAÇA
# 03/11/2014
# EXERCÍCIO 2

__author__ = 'davidvilaca'

'''
FUNCAO RECEBE COMO PARAMETRO LISTA(VETOR)
NAO RETORNA NADA POIS VETORES SAO MUTAVEIS
'''
def f_ordena(vetor):
	
	#variaveis locais
	contador = 0
	
	contador = (len(vetor))-1
	#print
	while contador >= 0:
		print(vetor[contador])
		contador -= 1
	
		
	return 0
		
		
	
#--fim f_ordena--

def main():
	#variaveis
	lista = []; cont = "";
	
	#entrada de dados
	cont = input('Insira um elemento para a lista ou "fim" para encerrar a insercao: ')
	while cont != "fim":
		lista.append(cont)
		cont = input('Insira um elemento para a lista ou "fim" para encerrar a insercao: ')
	
	#ordenar
	f_ordena(lista)
	
	return 0
#--fim main--


if __name__ == '__main__':
	main()
#--fim if--
