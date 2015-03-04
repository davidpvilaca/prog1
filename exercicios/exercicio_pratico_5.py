#  22/10/2014
#  Exercício prático 5
#  
#  lendo dois valores reais x e y do teclado e mostre o valor da expressão
#  



import math

def main():
	#Declarando variável
	x = 0
	y = 0
	z = 0
	
	#Definindo valor das variáveis
	x = float ( input ('x=') )
	y = float ( input ('y=') )
	
	#Calculando
	z = math.sqrt((x**2)-(y**2))
	
	#Mostrando o resultado
	print (' O resultado é %.2f' %(z))
	return 0

if __name__ == '__main__':
	main()
