# EXERCÍCIO - LABORATÓRIO - 03
#
# DAVID PANTALEÃO VILAÇA | TADEU DA PENHA MORAES JUNIOR
#
#  Faça um programa que leia do teclado a data de nascimento (valores d, m e a) de uma pessoa e a
# data atual. Calcule e mostre a idade da pessoa em dias, meses e anos. Verifique e mostre, tamb´em,
# se ela j´a tem idade suficiente para tirar carteira de habilita¸c˜ao e votar. Observa¸c˜oes: Ignore os anos
# bissextos, ou seja, 1 ano equivale a 12 meses que equivale a 365 dias.


#funcao main
def main():

    print('DESCUBRA SE SE VOCE PODE TIRAR HABILITACAO')

    #Declaracao de variavel
    d, m, a, da, ma, aa = 0,0,0,0,0,0
    af, mf, df = 0,0,0

    #Entrada de dados
    da = int (input('Digite o dia atual: '))
    ma = int (input('Digite o mes atual: '))
    aa = int (input('Digite o ano atual: '))

    d = int (input('\nDigite o dia em que voce nasceu: '))
    m = int (input('Digite o mes em que voce nasceu: '))
    a = int (input('Digite o ano em que voce nasceu: '))

    #processamento

    af = aa-a
    
    #se o mes atual for maior que o mes do aniversario
    if m < ma:
        mf = ma - m
        
    #se o mes do aniversario for maior que o mes atual
    elif m > ma:
        af -= 1 #Neste caso a pessoa ainda nao aniversariou no ano atual entao retiro 1 ano
        mf = (ma-m)+12 #se apenas calcular (ma-m) teremos o restante que falta para o aniversario, entao somamos 12 (que é um ano quer retiramos acima)
    #fim if

    #se o dia atual for maior que o dia do aniversario
    if d < da:
        df = da-d
    
    #se o dia do aniversario for maior que o dia atual
    elif d > da:
        mf -= 1 #neste caso retiramos 1 mes pois ainda não foi totalmente completado ele
        
        #condicao para meses com 31 dias
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            df = (da-d)+31 #igual ao caso acima do mes, porem somando 31 que sao os dias do mes neste if
            
        #se o mes for fevereiro consideramos que ele tem 28 dias (enunciado da questao)
        elif m == 2:
            df = (da-d)+28
        
        #condicao para meses com 30 dias
        elif m == 4 or m == 6 or m == 9 or m == 11:
            df = (da-d)+30
        #fim if
    #fim if

    print ('\n%d anos e %d meses e %d dias\n' %(af,mf,df))

    if af >= 16 and af < 18:
        print('Voce tem idade suficiente para votar, mas nao para tirar a carteira de habilitacao!\n')
    elif af < 16:
        print('Voce nao tem idade suficiente para votar nem para tirar a carteira de habilitacao!\n')
    elif af >= 18:
        print('Voce tem idade suficiente para votar e tambem para tirar a carteira de habilitacao!\n')
    #fim if

    return 0
    
#fim main

if __name__ == '__main__':
    main()
#fim if
