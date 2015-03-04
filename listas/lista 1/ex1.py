# EXERCÍCIO - LABORATÓRIO - 01
#
# DAVID PANTALEÃO VILAÇA | TADEU DA PENHA MORAES JUNIOR
#
# Receba como entrada três números e os imprime em ordem crescente


#FUNÇÃO MAIN
def main():
  #Declaração de variáveis
  a = 0
  b = 0
  c = 0
  
  #Entrada de dados
  a = float ( input('Insira um número:') )
  b = float ( input('Insira outro número:') )
  c = float ( input('Insira outro número:') )
  
  
  #Processamento de dados
  print ('Os números em ordem crescente são:')
  
  if a>b and a>c:
    
    if c>b:
      print (b)
      print (c)
    else:
      print (c)
      print (b)
      
    print (a)
    
    
  if b>a and b>c:
    if c>a:
      print (a)
      print (c)
    else:
      print (c)
      print (a)
      
    print (b)
    
    
  if c>a and c>b:
    if a>b:
      print (b)
      print (a)
    else:
      print (a)
      print (b)
      
    print (c)
    
  return 0

#FIM MAIN
if __name__ == '__main__':
	main()
#FIM IF

