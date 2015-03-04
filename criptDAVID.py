# CRIPTOGRAFIA E DESCRIPTOGRAFIA
# DAVID VILAÇA
# 13/11/2014


def main():
  
  #Declaração de variáveis
  mensagem, funcao = "",0
  mensagemcript = ""
  contador = 0
  aux, aux2, aux3 = "",0,""
  alfa = "abcdefghijklmnopqrstuvwxyzç0123456789?! "
  enc  = "wcvzxboghmjkanfçiqyseuptrd!5791302846?! "
  
  #print inicial
  print('/////////////////////////////////////////////')
  print('/CRIPTOGRAFAR E DESCRIPTOGRAFAR UMA MENSAGEM/')
  print('/////////////////////////////////////////////\n\n')
  print('FUNÇÕES:\n1 - CRIPTOGRAFAR\n2 - DESCRIPTOGRAFAR\n3 - SAIR\n')
  #fim print
  
  
  #PROCESSAMENTO/entrada de dados
  funcao = int(input('Digite a função desejada: '))
  while funcao < 1 or funcao > 3:
    funcao = int(input('Função inválida, digite novamente: '))
    
  if funcao == 1: #se o usuario escolher criptografar execulte o codigo abaixo
    print('\nCRIPTOGRAFAR UMA MENSAGEM')
    mensagem = input('Digite a mensagem a ser criptografada: ')
    mensagem = mensagem.lower() #garante que toda a string será minúscula
    
    
    if mensagem == "": #se não digitar mensagem
      print ('\nNenhuma mensagem digitada!')
      
    elif mensagem != "":  #se digitar mensagem
      
      while contador < int(len(mensagem)): #enquanto o contador for menor que o numero de caracteres da mensagem
        aux = mensagem[contador]  #variavel aux recebe a letra da mensagem que esta na posição que o contador indicar
        aux2 = int(alfa.find('%s' %(str(aux)))) #variavel aux2 encontra a posição da letra no alfabeto normal e armazena
        aux3 = enc[aux2] #variavel aux3 criptografa a letra que esta na posição indicada acima
        mensagemcript = mensagemcript+aux3  #a string relativa na variavel enc é armazenada junto da anterior
        contador += 1 #contador soma 1 a cada repetição para não ocorrer loop infinito
      #fim while
      
    print ("\nSua mensagem criptografada é:\n")
    print (mensagemcript,"\n")
      
    #fim if
  
  elif funcao == 2:
    print('\nDESCRIPTOGRAFAR UMA MENSAGEM')
    mensagemcript = input('Digite a mensagem a ser descriptografada: ')
    
    if mensagemcript == "":
      print ('\nNenhuma mensagem digitada!')
      
    elif mensagemcript != "":
      
      #AS MESMAS COISAS DA CRIPTOGRAFIA SO QUE AGORA BUSCANDO STRINGS DO ENC PARA ACHÁ-LAS NO ALFA
      while contador < int (len(mensagemcript)):
        aux = mensagemcript[contador]
        aux2 = int(enc.find('%s' %(aux)))
        aux3 = alfa[aux2]
        mensagem = mensagem+aux3
        contador += 1
      #fim while
      
      print ("\nSua mensagem é:\n")
      print (mensagem,"\n")
    
    #fim if
  
  elif funcao == 3:
    exit('\nAdeus!')
  
  #fim if
  
  
  
  return 0

if __name__ == '__main__':
	main()

