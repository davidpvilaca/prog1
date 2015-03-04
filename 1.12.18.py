#	13/11/2014
#	
#	1.12.18
#	
#	DAVID VILAÇA
#	PROBLEMA DO RALLYE


def main():
	
	#Declaração de variável
	tp1, tp2, tp3, inscr = 0,0,0,""
	temp1, temp2, temp3 = 0,0,0
	d1, d2, d3 = 0.0,0.0,0.0
	ponto1, ponto2, ponto3, pontot = 0,0,0,0
	totalg = 0.0
	inscrg = ""
	
	#Entrada de dados / Processamento
	print ('RALLYE\n')
	
	#entrada dos tempos-padrao
	tp1 = int ( input('Digite o tempo padrao 1: ') )
	tp2 = int ( input('Digite o tempo padrao 2: ') )
	tp3 = int ( input('Digite o tempo padrao 3: ') )
	
	inscr = "" #Valor de inicio da inscricao
	totalg = 0 #Valor de inicio da maior pontuacao (aqui nao foi cadastrada nenhuma equipe ou pontuacao as maiores irao substituir esse valor)
	
	print ('\nAgora digite os dados de cada equipe\n')
	
	#tabela do rallye	
	while inscr != "9999":  #loop enquanto a inscricao for diferente da string 9999
		inscr = input ('Insira a incricao ou "9999" para encerrar: ')   #recebendo a inscricao do teclado
		if inscr != "9999":
			
			temp1 = int (input('Tempo 1 da equipe:')) #entrada do primeiro tempo da equipe informada acima na inscricao
			d1 = abs(tp1-temp1) #delta calcula o valor absoluto, ou seja |x|, da diferenca tempo padrao para o tempo da equipe
			
      #calculo da pontuacao como exigido na questao
			if d1 < 3:
				ponto1 = 100
			elif d1 >= 3 and d1 <= 5:
				ponto1 = 80
			else:
				ponto1 = 80-(d1-5)/5
			#fim if
      
    #fim if
    
			temp2 = int (input('Tempo 2 da equipe:')) #entrada do segundo tempo da equipe informada acima na inscricao
			d2 = abs(tp2-temp2)
  
			if d2 < 3:
				ponto2 = 100
			elif d2 >= 3 and d2 <= 5:
				ponto2 = 80
			else:
				ponto2 = 80-(d2-5)/5
			#fim if
			
			temp3 = int (input('Tempo 3 da equipe:'))
			d3 = abs(tp3-temp3)
			
			if d3 < 3:
				ponto3 = 100
			elif d3 >= 3 and d3 <= 5 :
				ponto3 = 80
			else:
				ponto3 = 80-(d3-5)/5
			
			#pontuacao total
			pontot = ponto1+ponto2+ponto3
			
      #condicao de armazenagem para o maior valor da pontuacao total
			if pontot > totalg: #se a pontuacao total for maior que a pontuacao armazenada a variavel "totalg" armazena ela
				totalg = pontot
				inscrg = inscr
      #fim if
      			
			#saida de dados
			print ('\nINSCRICAO  |  PONTO1  |  PONTO2  |  PONTO3  |  PONTO_TOTAL')
			print ('    %s       %.2f      %.2F     %.2F       %.2F   \n' %(inscr,ponto1,ponto2,ponto3,pontot))
  #fim while
  
	print('\nRESULTADO FINAL:\n') 
			
	print ('VENCEDOR: %s com a pontuacao = %.2f\n' %(inscrg,totalg))  #Quando while acaba o resultado final e impresso na tela
		
	
	
	return 0
  
#fim main
if __name__ == '__main__':
	main()
#fim if
