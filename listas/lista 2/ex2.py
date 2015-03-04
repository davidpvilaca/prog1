__author__ = 'David_Tadeu'


def f_volume (raio):
    #variaveis locais
    volume = 0.0; pi = 3.14159265358979;

    #processamento
    volume = (4/3)*(pi)*(raio**3) #formula dada no enunciado

    return(volume)
#--fim f_volume--

def f_area (r):
    #variaveis locais
    area = 0.0; pi = 3.14159265358979;

    #processamento
    area = 4*(pi)*(r**2) #formula dada no enunciado

    return(area)
#--fim f_area--

def main():
    #variaveis
    r = 0.0; v = 0.0; a = 0.0;

    #entrada de dados
    print('CALCULO DO VOLUME E DA AREA DE UMA ESFERA\n\n')
    r = float(input('Insira o raio da esfera para o calculo: '))

    #chamada das funcoes de calculo
    v = f_volume(r)
    a = f_area(r)

    #saida de dados
    print('O volume eh %.2f e a area eh %.2f' %(v,a))

    return 0
#--fim main--

if __name__ == '__main__':
    main()
#--fim if--