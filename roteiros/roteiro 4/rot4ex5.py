# DAVID VILAÇA
# 26/11/2014
# EXERCÍCIO 4

import turtle

#recebe tres parametro inteiros
#retorna um desenho na biblioteca turtle
def f_lados (l,x,y):
	#variaveis internas
	ze = turtle.Turtle(); n = 0; i = 0
	
	ze.speed('fast')
	
	#ze.penup
	ze.goto(x,y)
	ze.dot(x,y)
	ze.forward(l)
	ze.pendown
	
	n = 360/l
	
	for i in range(l):
		ze.forward(n)
		ze.right(n)
		
	return (turtle.done())


def main():
	#declaracao de variaveis
	lados = 0; aux = 0; aux1 = 0; aux2 = 0;
	
	#entrada de dados
	lados = int (input('Digite o numero de lados, >= 3, do poligono: '))
	while lados < 3:
		lados = int (input('LADOS MAIOR OU IGUAL A 3: '))
	
	aux1 = int (input('Digite a coordenada X do centro: '))
	aux2 = int (input('Digite a coordenada y do centro: '))
		
	#processamento
	aux = f_lados(lados,aux1,aux2)
	
	
	return 0

if __name__ == '__main__':
	main()

