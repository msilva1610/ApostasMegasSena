
def CalculadezenasPrimos(volante):
    arrPrimos = []
    for numero in volante:
        divisores = 0
        for divisor in range(1, numero):
            if numero % divisor == 0:
                divisores = divisores + 1
                if divisores > 1:
                    break
        if divisores > 1:
            print("{} não é primo".format(numero))
        else:
            print("{} é primo".format(numero))
            arrPrimos.append(numero)
    print('Todos os primos: {}'.format(arrPrimos))

if __name__ == '__main__':
    volante = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
    CalculadezenasPrimos(volante)

