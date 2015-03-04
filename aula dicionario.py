#  AUla estruturas de dados heterogêneas


#Dicionário



def dicionario():
	
	#dicio
	dic = {}
	
	#insirindo valores
	dic[1] = "Joao" #Se não tiver a chave 1 ele cria
	
	#Acessando
	dic[1]
	print(dic[1])
	
	#FUncoes
	len(dic)
	
	dic.keys()
	
	return 0

def exemplo1():
	
	# matricula --> chave
	# [n1,n2,n3,trab,faltas,nome] --> valor
	
	ex = {"20142bsi0194": [15.0, 25.5, 50.0, 0.5,10,"David"]}
	
	
	return 0
	
# Faça uma função que cadastre (insira) alunos no dicionario
# do Exemplo 1.
def f_insereALuno(dicAluno):
	
	mat = "", nome=""
	n1, n2, n3, trab, faltas = 0.0,0.0,0.0,0.0,0
	
	mat = input("Informe a matricula do aluno: ")
	
	if mat in dicAluno:
		print("Aluno já cadastrado")
	else:
		n1 = float(input("Insira a nota 1: "))
		n2 = float(input("Insira a nota 2: "))
		n3 = float(input("Insira a nota 3: "))
		trab = float(input("Insira a nota do trabalho: "))
		faltas = int(input("Insira o número de faltas: "))
		lst = [n1,n2,n3,trab,faltas, nome]
		
		dicAluno[mat] = lst

#TUPLAS

def tuplas():
	
	#tupla vazia
	x = ()
	
	#nao pode usar append nem isert pois e imutavel
#-
	
	

if __name__ == '__main__':
	main()

