#letra A
def criaFracao(x,y):
	fracao = ()
	
	if y == 0:
		y = 1
	elif y < 0 :
		y = y * (-1)
		x = x * (-1)
	
	fracao = (x,y)
	
	return fracao

#letra b
def calculaMdc(dividendo,divisor):
	MDC = 0
	resto = 1
	while(resto !=0):
		if(dividendo % divisor != 0):
			resto = dividendo % divisor
			dividendo = divisor
			divisor = resto
			
		if(dividendo % divisor == 0):
			MDC = divisor
			resto = 0
	#fim while
	return MDC
	
'''
#letra C
def simplificaFrac(frac):
	aux = 0; simplificado = (); x, y = 0,0
	
	#pegando o maior valor e adicionando a variavel aux	
	if frac[0] < frac[1]:
		aux = frac[1]
	else:
		aux = frac[0]
	
	#i percorrendo de 1 ate aux
	for i in range(aux+1): #i+1 pra nao ter divisao por 0
		if (frac[0]%(i+1)) == 0 and (frac[1]%(i+1)) == 0: #pegando resto para ver se e divisivel
			x = frac[0]//(i+1)
			y = frac[1]//(i+1)
			
	simplificado = (x, y)
	
	return simplificado
'''
#letra C com MDC
def simplificaFrac(f):
	novaf = (); x = 0
	
	x = abs(calculaMdc(f[0],f[1]))
	novaf = criaFracao(f[0]//x,f[1]//x)
	
	return novaf
	
def main():
	
	fracao = criaFracao(5, 0)
	fracao  = simplificaFrac(fracao)
	
	print(fracao)
	
	return 0

if __name__ == "__main__":
	main()
