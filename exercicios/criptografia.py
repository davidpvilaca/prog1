# DAVID VILAÇA
# 
# 13/11/2014
# ESCREVA UM PROGRAMA QUE LEIA UMA MENSAGEM E CRIPTOGRAFA COM UMA CRIPTOGRAFIA À ESCOLHA.
# IMPRIMA A MENSAGEM CRIPTOGRAFADA!
#

#Função Main
def main():

  #Declaração de variáveis
  mensagem = ""
  mensagemcript = ""
  contador = 0
  aux, aux2, aux3 = "",0,""
  alfa = "abcdefghijklmnopqrstuvwxyzç "
  enc  = "wcvzxboghmjkanfçiqyseuptrd1 "

  print ('\n//////////////////////////')
  print ('/EMBARALHADOR DE MENSAGEM/')
  print ('//////////////////////////')

  mensagem = input ('\nDigite a mensagem a ser criptografada: ')
  
  mensagem = mensagem.lower() #se tiver maiuscula fica automaticamente minuscula pra achar na variavel enc
                              #porque maiuscula e minuscula tem diferença
  if mensagem == "":
    print ('\nNenhuma mensagem digitada!')
  elif mensagem != "":

    while contador < int(len(mensagem)):
      aux = mensagem[contador]
      aux2 = int(alfa.find('%s' %(str(aux))))
      aux3 = enc[aux2]
      contador += 1
      mensagemcript = mensagemcript+aux3
    
  
  print ("\nSua mensagem criptografada é:\n")
  print (mensagemcript,"\n")
  
  return 0
  
if __name__ == '__main__':
  main()
