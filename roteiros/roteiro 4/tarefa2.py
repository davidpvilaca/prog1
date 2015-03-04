# DAVID PANTALEAO VILACA
# ATIVIDADE AVALIATIVA - TAREFA 2
# 
# DATA: 10/11/2014
# 
# PROF. Alessandra Aguiar Vilarinho


#FUNCAO MAIN
def main():
  
  #DECLARACAO DE VARIAVEIS
  sexo, resposta, qtd, aux1, aux2, aux3, aux4, aux5, aux6, psm, pnm, psf, pnf, strpc, ts, tn = "","",0,0,0,0,0,0,0,0.0,0.0,0.0,0.0,"",0,0
  
  #ENTRADA DE DADOS/PROCESSAMENTO
  qtd = 0; aux1 = 0; aux2 = 0; aux3 = 0; aux4 = 0; aux5 = 0; aux6 = 0;
  print ('   PESQUISA DE MERCADO\n')
  print ('INFORME A SEGUIR O SEXO E A RESPOSTA DA SEGUINTE FORMA:\nSEXO (M, F) E RESPOSTA (S, N)\n')
  print ('*M = Masculino; F = Feminino; S = Sim; N = Não;\n*MAIUSCULO\n\n')
  
  while qtd < 4:
    qtd = qtd+1
    sexo = str(input ('Sexo:'))
    #CONDIÇÃO DE ENTRADA APENAS DE "F" OU "M"
    while sexo != "F" and sexo != "M":
      sexo = str(input ('Por favor digite a letra em MAIUSCULO referente ao sexo:'))
    #FIM WHILE SEXO
    
    resposta = input ('Resposta:')
    #CONDIÇÃO DE ENTRADA APENAS DE "S" OU "N"
    while resposta != "S" and resposta != "N":
      resposta = input ('Por favor digite a letra em MAIUSCULO referente à resposta:')
    #FIM WHILE RESPOSTA
    if sexo == "M":
      aux1 += 1
      if resposta == "S":
        aux2 += 1
      if resposta == "N":
        aux3 += 1
    if sexo == "F":
      aux4 += 1
      if resposta == "S":
        aux5 += 1
      if resposta == "N":
        aux6 += 1
  #fim while
  if aux1 != 0:
	  psm = (aux2*100)/aux1
	  pnm = (aux3*100)/aux1
  if aux4 != 0:
	  psf = (aux5*100)/aux4
	  pnf = (aux6*100)/aux4
  if aux1 == 0:
	  aux1 = 1
  if aux4 == 0:
	  aux4 = 1
  strpc = "%"
  ts = aux2+aux5
  tn = aux3+aux6

  #IMPRESSAO DOS RESULTADOS
  print ('\n RESULTADOS OBTIDOS:\n')
  print ('Qtd sexo masulino: %d;\nQtd sexo feminino:%d;\n' %(aux1,aux4))
  print ('SEXO MASCULINO:\n SIM: %d  (%.2f%s)\n NAO: %d  (%.2f%s)\n' %(aux2,psm,strpc,aux3,pnm,strpc))
  print ('SEXO FEMININO:\n SIM %d  (%.2f%s)\n NAO: %d  (%.2f%s)' %(aux5,psf,strpc,aux6,pnf,strpc))
  print ('\nQtd total de "sim": %d\nQtd total de "nao": %d' %(ts,tn) )
  #FIM DA IMPRESSAO
    
  return 0

#FIM MAIN
if __name__ == '__main__':
	main()
#FIM IF

