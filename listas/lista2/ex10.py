# DAVID VILAÇA
# 13.12.2014
# EXERCÍCIO 10

'''
F_UNIAO ENTRA COM PARAMETRO L1 E L2 (LISTAS) DE INTEIROS
RETORNA U (LISTA) QUE EH A UNIAO DE L1 E L2
'''
def f_uniao(l1,l2):
	#variaveis locais
	i, taml1, taml2, u = 0,0,0,[]
	
	taml1, taml2 = len(l1),len(l2)
	
	#processamento
	for i in range(taml1):
		if l1[i] not in u:
			u.append(l1[i])
		# -- fim if--
	#--fim for--
	for i in range(taml2):
		if l2[i] not in u:
			u.append(l2[i])
		#--fim if--
	#--fim for--
	
	return u

'''
F_INTERSECAO ENTRA COM PARAMETRO L1 E L2 (LISTAS) DE INTEIROS
RETORNA I (LISTA) QUE EH A INTERSECAO DE L1 E L2
'''
def f_intersecao(l1,l2):
	#variaveis locais
	j, k, taml1, taml2 = 0,0,0,0
	i = []
	
	taml1, taml2 = len(l1),len(l2)
	
	#processamento
	for j in range(taml1):
		for k in range(taml2):
			if l1[j] == l2[k]:
				if l1[j] not in i:
					i.append(l1[j])
				#--fim if--
			#--fim if--
		#--fim for--
	#--fim for--
	
	return i

def main():
	#variaveis
	a, b = [], []
	u,i = [],[]
	
	#entrada de dados
	a = [1,2,4,6,8]
	b = [3,5,7,9,1,9]
	
	#criar uniao e intersecao de a e b
	u = f_uniao(a,b)
	i = f_intersecao(a,b)
	
	#saida de dados
	print(a)
	print(b,end='\n\n')
	print('Uniao: ', end=''); print(u)
	print('Intersecao: ',end=''); print(i)
	
	return 0
#--fim main--

if __name__ == '__main__':
	main()
#--fim if--
