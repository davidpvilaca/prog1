# EXERCÍCIO - LABORATÓRIO - 08
#
# DAVID PANTALEÃO VILAÇA | TADEU DA PENHA MORAES JUNIOR
#
#  Escreva um programa que leia 10 valores inteiros e encontre o maior e o menor dentre esses valores.
# O programa deve mostrar o resultado dos valores encontrados na tela.
# Observacao: use um comando
# de repeticao.


#funcao main
def main():
  
  
  print ('DESCUBRA O MAIOR INTEIRO DIGITANDO 10 NUMEROS ABAIXO:') #print inicial/informacao
  
  #declaracao de variaveis
  num, aux, aux2, contador = 0,0,0,0
  
  #entrada de dados
  
  contador = 1 #contador comecando com o valor 1
  
  #num recebe um numero inteiro do teclado
  num = int(input('%d - Insira um valor: ' %(contador)))
  aux = num
  aux2 = num
  
  #processamento
  while contador < 10: #enquanto o contador for menor
    if aux < num: #se a aux for maior que o numero ela recebera o numero
      aux = num
      print ('\nO maior valor por enquanto é: %d\n' %(aux) ) #mostra o resultado como no enunciado
    if aux2 > num:
      aux2 = num
      print ('\nO menor valor por enquanto é: %d\n' %(aux2) ) #mostra o resultado como no enunciado
    contador += 1 #contador como condicao de parada do while
    num = int(input('%d - Insira um valor: ' %(contador))) #entrada dos proximos numeros dentro do loop
    
    
  print ('\n\nO maior valor informado e %d\n O menor valor informado e %d' %(aux,aux2) ) #impressao do resultado final
  
  
  return 0

#fim main
if __name__ == '__main__':
    main()
#fim if
