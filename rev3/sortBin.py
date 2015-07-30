__author__ = 'ifes'


def fazBuscaBin(lst, elem):
    meio = 0
    inicio = 0
    fim = len(lst) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lst[meio] == elem:
            inicio = fim + 1
        elif lst[meio] > elem:
            fim = meio - 1
        else:
            inicio = meio + 1
            # -fim if
    # -fim while
    if lst[meio] == elem:
        return meio
    else:
        return -1
        #-fim if


# -fim fazBuscaBin


def fazBuscaBinR(lst, elem, _tentativa=0, _inicio=0, _fim=-1):
    if _fim == -1:
        _fim = len(lst)-1
    meio = (_inicio + _fim) // 2
    aux_num = lst[meio]
    if _tentativa == len(lst)-1:
        return -1
    if elem == aux_num:
        return meio
    elif elem > aux_num:
        _inicio = meio+1
        return fazBuscaBinR(lst, elem,  _tentativa= _tentativa+1,_inicio=_inicio, _fim=_fim)
    else:
        _fim = meio-1
        return fazBuscaBinR(lst, elem,  _tentativa= _tentativa+1,_inicio=_inicio, _fim=_fim)
#-
def main():
    test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(fazBuscaBinR(test, 4))
    print(fazBuscaBin(test,4))
    print(test.index(4))

    return 0


if __name__ == '__main__':
    main()
