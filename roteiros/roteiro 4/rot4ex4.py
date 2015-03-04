# DAVID VILAÇA
# 26/11/2014
# EXERCÍCIO 4

import turtle

#recebe um parametro inteiro
#retorna um desenho na biblioteca turtle
def f_lados (x):
	#variaveis internas
	ze = turtle.Turtle(); n = 0; i = 0
	
	ze.speed('fast')
	
	n = 360/x
	
	for i in range(x):
		ze.forward(n)
		ze.right(n)
		
	return (turtle.done())


def main():
	#declaracao de variaveis
	lados = 0; aux = 0
	
	#entrada de dados
	lados = int (input('Digite o numero de lados, >= 3, do poligono: '))
	while lados < 3:
		lados = int (input('LADOS MAIOR OU IGUAL A 3: '))
		
	#processamento
	aux = f_lados(lados)
	
	
	return 0

if __name__ == '__main__':
	main()

