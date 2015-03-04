__author__ = 'David_Tadeu'

'''
F_SOMA RECEBE O PARAMETRO NUM DO TIPO INTEIRO
RETORNA SOMA DO TIPO INTEIRO
'''
def f_soma(num):
    #variaveis locais
    aux = 1;  soma = 0;

    #processamento
    while aux <= num: #Enquanto a aux for menor que o numero lido do teclado no main
        soma = soma+aux
        aux += 1

    return(soma)
#--fim f_soma--

def main():
    #variaveis
    n = 0; sn = 0;

    #entrada de dados
    print('Soma do intervalo\n\n')
    n = int(input('Insira um numero inteiro: '))

    #chamando funcao de soma
    sn = f_soma(n)

    #saida de dados
    print('A soma do intervalo de 1 ate %d eh %d' %(n,sn))

    return 0
#--fim main--

if __name__ == '__main__':
    main()
#--fim if--