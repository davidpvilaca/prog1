# DAVID VILAÇA
# 26/11/2014
# EXERCÍCIO 3

#funcao entra com parametros float
#retorna s float

def calcula_s (a,b):
	#variaveis internas
	s = 0.0
	#processamento
	s = a-((a*b)**0.5)+(b**2)
	
	return (s)
	

def main():
	
	#declaracao de variaveis
	x, y = 0.0,0.0
	aux = 0.0
	
	#entrada de dados
	x = float(input('Digite um valor para x: '))
	y = float(input('Digite um valor para y: '))
	
	#processamento
	if x > 0 and y < 0:
		print ('\nSolucao no dominio dos numeros complexos!\n')
	elif x < 0 and y > 0:
		print ('\nSolucao no dominio dos numeros complexos!\n')
	else:
		aux = calcula_s(x,y)
		#saida de dados
		print('\nO resultado é =~ %.2f \n'%(aux))
	
	
	return 0

if __name__ == '__main__':
	main()

