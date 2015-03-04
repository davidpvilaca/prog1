# DAVID VILAÇA
# 05/11/2014
# EXERCÍCIO 4 -  


def main():
	#DECLARAÇÃO DE VARIÁVEIS
	num = 0
	a = 0
	b = 0
	c = 0
	
	#ENTRADA DE DADOS
	num = int (input('Insira um número de 4 dígitos para verificarmos:') )
	
	#ESTRUTURA DE CONTROLE
	a = num//100
	b = num%100
	c = (a+b)**2
	if c != num:
		print ('O número informado não possui a característica!')
	else:
		print ('O número informado POSSUI a característica!')
	
	
	#SAÍDA DE  DADOS
	
	
	
	return 0

if __name__ == '__main__':
	main()

