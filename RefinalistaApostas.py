import json
import sys
import datetime

from GeraTodasApostas import Apostas

def CalculaMultiplos(dezenas):
    tot_m = 0
    multiplos = {}
    multiplos['de'] = []    
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


def ValidaFibonacci(dezenas):
    totFibo = 0
    Fibonacci = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    for d in dezenas:
        if d in Fibonacci:
            totFibo += 1
    return totFibo


def ValidaDezenaNoQuadrante(dezenas):
    qtde_q1, qtde_q2,qtde_q3, qtde_q4 = 0, 0, 0, 0
    quadrante = {}
    quadrante['quadrantes'] = []
    q1 = {1,2,3,4,5,11,12,13,14,15,21,22,23,24,25}
    q2 = {6,7,8,9,10,16,17,18,19,20,26,27,28,29,30}
    q3 = {31,32,33,34,35,41,42,43,44,45,51,52,53,54,55}
    q4 = {36,37,38,39,40,46,47,48,49,50,56,57,58,59,60}
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


def ContaPrimos(dezenas):
    NumerosPrimos = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
    totPrimos = 0
    for d in dezenas:
        if d in NumerosPrimos:
            totPrimos += 1
    return totPrimos


def SomaDigitosDezenas(dezenas):
    soma_dos_digitos_das_dezenas = 0
    for d in dezenas:
        strdezena = str(d)
        for s in strdezena:
            soma_dos_digitos_das_dezenas += int(s)
    return  soma_dos_digitos_das_dezenas


def SomaDezenas(dezenas):
    soma = 0
    for d in dezenas:
        soma += d
    return soma


def CalculaParImparSomaDez(dezenas):
    impares = 0
    pares = 0
    SomaDezenas = 0
    for d in dezenas:
        if d % 2 != 0:
            impares += 1
        else:
            pares += 1
        SomaDezenas += d
    return impares, pares, SomaDezenas     


def ValidaApostas(ListaDeApostas):
    '''
    Valida Aposta: 
        Impares e Pares Duração: 0:02:53.174411
        Com soma Dezenas: 0:03:21.039748
        Até o Valida fibonacci o tempo médio para 1.000k é de 12 segundos
    '''
    tot = 0
    idAposta = 0
    ListaRefinada = {}
    ListaRefinada['apostas'] = []
    TempoInicialLote = datetime.datetime.now()
    print('Loop nas apostas iniciado...{}'.format(datetime.datetime.now()))
    for aposta in ListaDeApostas:
        idAposta += 1
        tot += 1
        # Remove parentenses por chaves. com chaves n'ao gera erro no json
        aposta = list(aposta)
        # 01 e 02 Calcula Dezenas Impares e Pares - 04 Soma dezenas
        impares, pares, somadasdezenas = CalculaParImparSomaDez(aposta)
        # 05 Soma digitos das Dezenas
        SomaDosDigitosDaDezena = SomaDigitosDezenas(aposta)
        # 06 Total de Numeros Primos nas dezenas
        TotalDePrimos = ContaPrimos(aposta)
        # 06 Dezenas nos Quadrantes
        # q = 0
        q = ValidaDezenaNoQuadrante(aposta)
        # 07 Valida Fibonacci
        # qtdeDezFinonacci = 0
        qtdeDezFinonacci = ValidaFibonacci(aposta)
        # 08 Valida se dezenas tem multiplos

        multiplos = CalculaMultiplos(aposta)

        ListaRefinada['apostas'].append({
            'id': idAposta, 'aposta': aposta, 'impares': impares, 'pares':pares, 'SomaDasDezenas':somadasdezenas, 'SomaDosDigitosDaDezena':SomaDosDigitosDaDezena, 'TotalDePrimos': TotalDePrimos, 'Quadrantes': q,
            'DezenasFibonacci': qtdeDezFinonacci, 'multiplos':multiplos['de']
            })
        #if tot == 1000000:
        if tot == 10000:
            TempoFinalLote = datetime.datetime.now()
            TempoLote = TempoFinalLote - TempoInicialLote
            print('{} Apostas validadas. Tempo do lote {} - Hora: {}'.format(idAposta,TempoLote,datetime.datetime.now()))
            tot = 0
            TempoInicialLote = datetime.datetime.now()
            break
    return ListaRefinada

if __name__ == '__main__':
    dezenas = 6
    inicio = datetime.datetime.now()
    print('inicio ...{}'.format(inicio))
    print('calculando apostas ...{}'.format(datetime.datetime.now()))
    clsApostas = Apostas()
    ListaDeApostas = clsApostas.CalculaApostas(dezenas)

    ListaApostasValidada = ValidaApostas(ListaDeApostas)
    # print(ListaApostasValidada)
    fim = datetime.datetime.now()
    print('fim ...{}'.format(fim))
    print('duracao ...{}'.format(fim-inicio))
    print(ListaApostasValidada['apostas'][0])
    
