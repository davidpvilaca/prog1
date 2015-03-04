# DAVID VILAÇA
# 26/11/2014
# EXERCÍCIO 1

#equacao de segundo grau
#entra a, b e c ambos inteiros
#retorna x1 e/ou x2 ambos float

def f_eq (a,b,c):
	#variaveis locais
	delta = 0.0
	
	#processamento
	delta = (b**2)-4*a*c
	
	return (delta)
	


def main():
	
	#declaracao de variaveis
	num1, num2, num3 = 0.0,0.0,0.0
	aux = 0.0
	
	#Entrada de dados
	num1 = float(input('Digite o valor de a: '))
	num2 = float(input('Digite o valor de b: '))
	num3 = float(input('Digite o valor de c: '))
	
	#Processamento
	aux = f_eq (num1, num2, num3)
	
	print('Delta = %.3f' %(aux))
	
	
	return 0

if __name__ == '__main__':
	main()

