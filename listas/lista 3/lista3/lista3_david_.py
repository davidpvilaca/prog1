# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 22:03:19 2015

@author: david
"""
#---------------------------------------------#


'''
Funcao auxiliar de verificacao de listas para o exercicio 3
'''
def f_verificaAtores(filmeA, filmeB, ator):
    i, j = 0,0
    
    for i in range(len(filmeA)):
        for j in range(len(filmeB)):
            if ator == filmeA[i] and ator == filmeB[j]:
                return True
            
    
    return False
#------------- fim f_verificaAtores --------------#
'''
Funcao auxiliar de verificacao
'''
def f_verificaKeys(filme, ator):
    i = 0
    
    for i in range(len(filme)):
        if ator == filme[i]:
            return True
    
    return False
#--------------- fim f_verificaKeys --------------#



#Exercicio 01
'''
Funcao recebe como parametro:
d = dicionario | f = nome de um filme | n = nome de um ator do filme indicado
'''
def f_insereAtualiza(d,f,n):
    i, keys = 0,[]
    
    keys = list(d.keys())
    
    if keys != []:
        while i < len(keys):
            if keys[i] == f:
                d[f].append(n)
                i = len(keys)
            elif i == len(keys)-1:
                d[f] = [n]
            i += 1
        #-
    else:
        d[f] = [n]
#-------------- fim f_insereAtualiza --------------#


'''
Funcao de criacao da base de dados (dicionario)
'''
#Exercicio 02
def f_criaDados():
    
    bancoDic, ator, filme = {},"",""
    
    print("PREENCHA ABAIXO A BASE DE DADOS\n")
    
    filme = input("Insira o nome de um filme para cadastrar ou enter para encerrar: ")
    while filme != "":
        ator = input("Insira o nome de um(a) ator/atriz do filme %s ou enter para encerrar: " %(filme))
        while ator != "":
            f_insereAtualiza(bancoDic,filme,ator)
            ator = input("Insira o nome de um(a) ator/atriz do filme %s ou enter para encerrar: " %(filme))
        filme = input("Insira o nome de um filme para cadastrar ou enter para encerrar: ")
    
    return bancoDic
#----------------- fim f_criaDados -----------------#


'''
Funcao recebe como parametro:
A e B = LISTA DOS ATORES INDICADOS PELO NOME | C = CODIGO DA OPERACAO (INT)
'''
#Exercicio 03
def f_operacao(a,b,c):
    i = 0
    
    if c == 1:
        print("Atores que apareceram nos filmes indicados:")
        for i in range(len(a)):
            print(a[i])
        for i in range(len(b)):
            if not f_verificaAtores(a,b,b[i]):
                print(b[i])
    elif c == 2:
        print("Atores que apenas apareceram nos dois filmes indicados:")
        for i in range(len(a)):
            if f_verificaAtores(a,b,a[i]):
                print(a[i])
    elif c == 3:
        print("Atores que apareceram em apenas um dos dois filmes indicados:")
        for i in range(len(a)):
            if not f_verificaAtores(a,b,a[i]) and not f_verificaAtores(a,b,b[i]):
                print(a[i])
        for i in range(len(b)):
            if not f_verificaAtores(a,b,b[i]) and not f_verificaAtores(a,b,b[i]):
                print(b[i])
    else:
        print("ERRO! A FUNCAO INDICADA NAO EH VALIDA!")

#----------- fim f_operacao --------------#


'''
Funcao recebe como parametro
n = nome do filme | d = dicionario
'''
#Exercicio 04
def f_atorContracena(n,d):
    
    keys, i, j = [], 0, 0
    impresso = []
    
    keys = list(d.keys())
    
    for i in range(len(keys)):
        if f_verificaKeys(d[keys[i]],n):
            for j in range(len(d[keys[i]])):
                if n != d[keys[i]][j] and not f_verificaKeys(impresso,d[keys[i]][j]):
                    print(d[keys[i]][j])
                    impresso.append(d[keys[i]][j])
    
    

#Exercicio 05
def main():
    
    d, filmeA, filmeB, ator, cod = {}, "", "", "", 0
    testar = 0
    
    print("TESTE DAS FUNCOES\n\nCOMANDOS:\n1 - Testar exercicios 1 e 2\n2 - Testar exercicio 3\n 3 - Testar exercicio 4")
    print("Para sair do teste digite um numero maior que 3 ou menor que 1\n")
    
    testar = int(input("Insira uma opcao de teste: "))
    while testar > 0 and testar < 4:
        
        if testar == 1:
            d = f_criaDados()
        
        elif testar == 2:
            cod = int(input("Digite um codigo valido para testar o exercicio 3: "))
            filmeA = input("Digite o nome de um filme: ")
            filmeB = input("Digite o nome de outro filme: ")
            f_operacao(d[filmeA],d[filmeB],cod)
            
        elif testar == 3:
            ator = input("Digite o nome de um ator: ")
            f_atorContracena(ator,d)
        
        testar = int(input("Insira uma opcao de teste: "))
        
    return 0
    
if __name__ == "__main__":
    main()