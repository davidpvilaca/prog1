#  DAVID VILACA
#  ATIVIDADE PROPOSTA 09.12.2014

__author__ = 'David'

def f_correcao(gab,resp):
	#variaveis locais
	i = 0; tam = 0; acertos = 0; erros = 0;
	tam = len(resp)
	
	#processamento
	for i in range(tam):
		if resp[i] == gab[i]:
			acertos += 1
		else:
			erros += 1
	#--fim for--
	f_pontoeprint(acertos,erros)	
	
	return (acertos)
#--fim f_correcao--

def f_pontoeprint (c,e):
	#variaveis locais
	pc = 0.0; pe = 0.0;
	#processamento
	pc = (c*100)/(c+e)
	pe = (e*100)/(c+e)
	#saida de dados
	print ('Acertos: %.2f%%\nErros:%.2f%%' %(pc,pe))
	print ('Pontuacao total: %d' %(c))
#--fim f_pontoeprint--

def f_frequencia (notasT,nota):
	#variaveis locais
	i = 0; cont = 0
	#processamento
	for i in notasT:
		if i == nota:
			cont += 1

	return (cont)
	
#--fim f_frequencia--

def main():
	#Variaveis
	qtdQ = 0; gabarito = []; mat = ""; respostas = []; i = 0; aux = ""; gravapontos = [];
	
	#ENTRADA DE DADOS
	
	print('CONTROLE DE PROVAS\n\n')
	qtdQ = 10
	print('Preencha o gabarito logo abaixo\n')
	
	#entrada do gabarito#
	for i in range(qtdQ):
		aux = input('Digite a alternativa correta da questao %d: ' %(i+1))
		while aux != 'a' and aux != 'b' and aux != 'c' and aux != 'd' and aux != 'e':
			aux = input('Gabarito preenchido errado! Digite novamente: ')
		gabarito.append(aux)
	#--fim da entrada do gabarito--#
	
	print('\nAGORA DIGITE OS DADOS DOS ALUNOS\n\n')
	
	i = 0
	aux = ""
	
	#entrada da matricula e respostas#
	mat = input('\nMatricula ou "fim" para encerrar: ')
	while mat != "fim":
		respostas = []
		for i in range(qtdQ):
			aux = input('Resposta da questao %d do aluno %s: ' %(i+1,mat))
			while aux != 'a' and aux != 'b' and aux != 'c' and aux != 'd' and aux != 'e':
				aux = input('Opcao invalida, digite novamente: ')
			#--fim while--
			respostas.append(aux)
		#--fim for--
		gravapontos.append(f_correcao(gabarito,respostas))
		mat = input('\nMatricula ou "fim" para encerrar: ')
	#--fim while--
	#--fim entrada da matricula e respostas--#

	#frequencia de cada nota#
	i = 0
	print('\nA FREQUENCIA DAS NOTAS\n\n')

	for i in range(qtdQ+1):
		print('Nota: %d -- %d Alunos'%(i,f_frequencia(gravapontos,i)))
	# --fim for

	# --fim frequencia de cada nota--
	
	return 0

if __name__ == '__main__':
	main()
