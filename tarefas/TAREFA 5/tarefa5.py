__author__ = 'david'

def f_criaFracao(n,d):

    if d == 0:
        d = 1
    if ((d < 0) and (n > 0)) or ((d < 0) and (n < 0)):
        d = d*(-1)
        n = n*(-1)

    return (n,d)

def f_mdc(n1, n2):

    #Colocando o maior numero como divisor
    if n1 > n2:
        dividendo = n1
        divisor = n2
    else:
        dividendo = n2
        divisor = n1
    #-
    #calculo mdc
    resto = dividendo%divisor
    while resto != 0:
        dividendo = divisor
        divisor = resto
        resto = dividendo%divisor
    #-
    return divisor

def f_simplifica(fracao):
    n1 = fracao[0]
    n2 = fracao[1]
    mdc = f_mdc(n1, n2)
    return (n1//mdc,n2//mdc)

def f_somaFracoes(frac1, frac2):
    mdc = f_mdc(frac1[1],frac2[1])
    somaN1 = (frac1[1]//mdc)*frac1[0]
    somaN2 = (frac2[1]//mdc)*frac2[0]
    soma = somaN1+somaN2
    return f_simplifica((soma,mdc))

def f_subtracaoFracoes(frac1, frac2):

    mdc = frac1[1]*frac2[1]
    subtracao = (frac1[1]*frac2[0])-(frac2[1]*frac1[0])
    fracNova = f_criaFracao(subtracao,mdc)
    if subtracao == 0:
        return fracNova
    else:
        fracNova = f_simplifica(fracNova)
        return fracNova

def f_multiplicaFracoes(frac1, frac2):
    multiplicada = ()
    multiplicada = (frac1[0]*frac2[0],frac1[1]*frac2[1])

    return f_simplifica(multiplicada)

def f_divideFracoes(frac1,frac2):

    invSegunda = f_criaFracao(frac2[1],frac2[0])

    return f_multiplicaFracoes(frac1,invSegunda)

def f_verificaImpropria(frac):

    if frac[0] < frac[1]:
        return False
    else:
        return True

def f_imprime_fracao(frac):

    print("%d/%d"%(frac[0],frac[1]), end=' ')



def main():

    frac1 = f_criaFracao(int(input("Insira um numerador para a fracao 1: ")), int(input("Insira um denominador para a fracao 1: ")))
    print("\n")
    frac2 = f_criaFracao(int(input("Insira um numerador para a fracao 2: ")), int(input("Insira um denominador para a fracao 2: ")))

    frac3 = f_somaFracoes(frac1,frac2)
    frac4 = f_subtracaoFracoes(frac1,frac2)
    frac5 = f_multiplicaFracoes(frac1,frac2)
    frac6 = f_divideFracoes(frac1,frac2)

    f_imprime_fracao(frac1)
    f_imprime_fracao(frac2)
    f_imprime_fracao(frac3)
    f_imprime_fracao(frac4)
    f_imprime_fracao(frac5)
    f_imprime_fracao(frac6)

    return 0

if __name__ == "__main__":
    main()