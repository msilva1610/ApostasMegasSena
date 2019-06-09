def CalculaMultiplos(dezenas):
    tot_m = 0
    for m in range(2,31):    
        tot_m = 0
        for d in dezenas:
            if d >= m:
                if d % m == 0:
                    #Essa dezena (d) é multiplo de m
                    tot_m += 1
        if tot_m > 1:
            multiplos['de'].append({str(m):tot_m})
    return multiplos

if __name__ == '__main__':
    ListaRefinada = {}
    ListaRefinada['apostas'] = []
    multiplos = {}
    multiplos['de'] = []
    ListaRefinada['apostas'].append({
        'id': 1, 'dezenas': [1, 2, 3, 4, 5, 6], 'impares': 3, 'pares': 3, 'SomaDasDezenas': 21,'multiplos':multiplos['de']})    
    aposta = [1,2,3,4,5,6]
    print(CalculaMultiplos(aposta))
    print(ListaRefinada)
 
