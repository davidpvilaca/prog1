#	
#	DAVID VILACA
#	LISTA 3
#	
#	EXERCICIOS
#	

__author__ = 'David Vilaca'

'''
Exercicio 1
parametros: d = dicionario  |  f = nome do  filme  | n = nome do ator/atriz
'''
def f_inserirInfo(d, f, n):
	if f not in d:
		d[f] = [n]
	else:
		d[f].append(n)
		

'''
Exercicio 2
'''
def f_cadastrarInfo():
	filme, atores, d = "", "", {}
	
	filme = input("Insira o nome de um filme ou enter para encerrar: ").lower()
	while filme != "":
		print("\nInsira agora os nomes dos atores/atrizes\n")
		atores = input("Nome do(a) ator/atriz ou enter para encerrar a insercao de atores: ").lower()
		while atores != "":
			f_inserirInfo(d, filme, atores)
			atores = input("Nome do(a) ator/atriz ou enter para encerrar a insercao de atores: ").lower()
		filme = input("\nInsira o nome de um filme ou enter para encerrar: ").lower()

	return d
	
'''
Exercicio 3
Parametros: a e b = nomes de filmes | c = codigo de operacao (int)
'''
def f_uniaoIntersecao(a,b,c):
	i = ""

	if c == 1:
		for i in a:
			print(i)
		for i in b:
			if i not in a:
				print(i)
	elif c == 2:
		for i in a:
			if i in b:
				print(i)

	elif c == 3:
		'''
		for i in a:
			if i not in b:
				print(i)
		for i in b:
			if i not in a:
				print(i)
		'''
		while i < len(a):
			for j in range(len(b)):
				if a[i] == b[j]:
					aux = a[i]
				if a[i] != aux:
			i+= 1


	return 0

'''
'''
def f_contracenou(n, d):
	i = ""; j = ""

	for i in d:
		if n in d[i]:
			for j in d[i]:
				if n != j:
					print(j)
				#-#-#-#-
			#-
		#-
	#-
	return 0

def main():
	
	#variaveis
	dicio = {}
	codigo = 0
	ator = ""
	filme1, filme2 = "", ""

	dicio = f_cadastrarInfo()

	
	return 0

if __name__ == '__main__':
	main()