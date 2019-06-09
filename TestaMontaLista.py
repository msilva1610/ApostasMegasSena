

def ValidaDezenaNoQuadrante(dezenas):
    qtde_q1, qtde_q2,qtde_q3, qtde_q4 = 0, 0, 0, 0
    quadrante = {}
    quadrante['quadrantes'] = []
    q1 = [1,2,3,4,5,11,12,13,14,15,21,22,23,24,25]
    q2 = [6,7,8,9,10,16,17,18,19,20,26,27,28,29,30]
    q3 = [31,32,33,34,35,41,42,43,44,45,51,52,53,54,55]
    q4 = [36,37,38,39,40,46,47,48,49,50,56,57,58,59,60]
    for d in dezenas:
        if d in q1:
            qtde_q1 += 1
        elif d in q2:
            qtde_q2 += 1
        elif d in q3:
            qtde_q3 += 1
        else:
            qtde_q4 += 1
    quadrante['quadrantes'] = {'qtde_q1': qtde_q1, 'qtde_q2': qtde_q2, 'qtde_q3': qtde_q3, 'qtde_q4': qtde_q4 }
    return quadrante

if __name__ == '__main__':
    ListaRefinada = {}
    ListaRefinada['apostas'] = []
    ListaRefinada['apostas'].append("aposta{'id': 1, 'aposta': (1, 2, 3, 4, 5, 6), 'impares': 3, 'pares': 3, 'SomaDasDezenas': 21}")
    aposta = [1,2,3,4,5,6]
    l = ValidaDezenaNoQuadrante(aposta) 
    print(l)
    ListaRefinada['apostas'].append(l)
    print(ListaRefinada)