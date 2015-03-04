# DAVID VILAÇA
# 03/11/2014
# EXERCÍCIO 8
import turtle
'''
F_DESENHA RECEBE CX E CY (LISTA) QUE SAO COORDENADAS PARA O TURTLE
NAO RETORNA NADA
'''
def f_desenha(cx,cy):
	#variaveis locais
	i = 0; tam = 0; desenha = turtle.Turtle();
	tam = len(cx) #o tamanho de X sera o mesmo que o tamanho de Y
	
	#processamento
	for i in range(tam):
		desenha.goto(cx[i],cy[i]) #o turtle vai para as coordenadas pertencentes nos elementos da lista
	#--fim for--
	turtle.done()

def main():
	#variaveis
	x = []; y = []; cont = 0
	
	#entrada de dados/processamento
	while cont != -999:
		cont = int (input('Insira uma coordenada X ou -999 para encerrar: '))
		if cont != -999:
			x.append(cont)
			y.append(int(input('Digite a coordenada Y:')))
		#--fim if--
	#--fim while--
	if x != []:
		f_desenha(x,y) #chama a funcao que desenha com turtle
	#--fim if--
	
	return 0
#--fim main--

if __name__ == '__main__':
	main()
#--fim if--
