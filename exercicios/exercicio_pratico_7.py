#  22/10/2014
#  Exercício prático 7
#  
#  
#  




def main():
	#Declarando variável
	x = 0
	y = 0
	ix = 0
	ix = 0
	#Definindo valor das variáveis
	x = int (input('Digite o valor de x:'))
	y = int (input('Digite o valor de Y:'))
	
	#Invertendo
	ix = y; iy = x; x = ix; y = iy;
	
	#Mostrando o resultado
	print ('VALORES INVERTIDOS:\n X=%d\n Y=%d' %(x,y))
	return 0

if __name__ == '__main__':
	main()

