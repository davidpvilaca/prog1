# DAVID VILAÇA
# 05/11/2014
# EXERCÍCIO 3 - RECEBER OS LIMITES E O VALOR DOS PIXEL E IMPRIMIR SE É VÁLIDO OU NÃO


def main():
	#DECLARAÇÃO DE VARIÁVEIS
	x = 0
	y = 0
	h = 0
	w = 0
	
	#ENTRADA DE DADOS
	print('Insira os limites h e w abaixo')
	h = int ( input('h:') )
	w = int ( input('w:') )
	print('Insira a largura e altura, respectivamente em x e y, abaixo')
	x = int ( input('x:') )
	y = int ( input('y:') )
	
	#ESTRUTURA DE CONTROLE
	if x >= 0 and y >= 0:
		if x <= h and y <= w:
			print ('O pixel é válido!')
		else:
			print ('O pixel excedeu o limite definido em h e w!')
		
	
	#SAÍDA DE  DADOS
	
	
	
	return 0

if __name__ == '__main__':
	main()

