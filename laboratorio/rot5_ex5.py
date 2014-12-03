# DAVID VILAÇA
# 03/11/2014
# EXERCÍCIO 5

'''
F_CALCULAMEDIA RECEBE VETOR(LISTA)
RETORNA A MEDIA(FLOAT)
'''
def f_calculamedia(vetor):
	#variaveis locais
	tam = 0; i = 0; media = 0.0;
	tam = len(vetor)-1
	#processamento
	while tam >= 0:
		media = media+vetor[tam]
		tam -= 1
	#--fim while--
	tam = len(vetor)
	if tam != 0:
		media = media/tam
	#--fim if--
	return(media)
#--fim f_calculamedia--

'''
F_IMPRIME RECEBE LISTA (VETOR) E M (FLOAT)
NAO RETORNA. APENAS IMPRIME E ENCERRA
'''
def f_imprime (lista, m):
	#variaveis locais
	tam = 0; aux = 0; eprint = 0.0
	tam = len(lista)
	#processamento
	for aux in range(tam):
		if lista[aux] > m:
			eprint = lista[aux]
			print ('%.2f - ACIMA DA MEDIA' %(eprint))
		
		elif lista[aux] < m:
			eprint = lista[aux]
			print ('%.2f - ABAIXO DA MEDIA' %(eprint))
		elif lista[aux] == m:
			eprint = lista[aux]
			print ('%.2f - NA MEDIA' %(eprint))
		#--fim if--
	#--fim for--
	return 0
#--fim f_imprime--


def main():
	#variaveis
	notas = []; econt = 0.0; media = 0.0
	
	#entrada de dados
	print('MEDIA DE NOTAS\n')
	econt = float (input('Insira a nota ou -1 para encerrar a insercao: '))
	while econt > 0:
		notas.append(econt)
		econt = float (input('Insira a nota ou -1 para encerrar a insercao: '))
	#--fim while--
	
	#calcula media
	media = f_calculamedia(notas)
	
	#impressao
	print('\n\n')
	f_imprime(notas,media)
	
	return 0
#--fim main--

if __name__ == '__main__':
	main()
#--fim if--
