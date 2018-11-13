# -*- coding: cp1252 -*-
import locale
from datetime import date, timedelta
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np


class Investimento(object):
    def __init__( self, capital, prazo, aporte, diaZero=date.today(), name=None, IR=False ):
        '''
            capital     - montante inicial
            prazo       - prazo em meses em que o dinheiro ficará aplicado
            aporte      - função que estipula os aportes mensais
            diaZero     - dia inicial da aplicação
            nome        - nome da aplicação
            IR          - False se a aplicação é livre de imposto de renda, True em caso contrário
            indexador   - 
        '''
        self.capital = capital
        self.montante = capital
        self.aporte = aporte
        self.prazo = prazo
        self.diaZero = diaZero
        self.name = name
        self.IR = IR

        
        self.dia = diaZero
        self.delta_dias = timedelta(30)                     # mensal

        self.montanteAcumulado = []
        self.datas = []

    def retornaDividendo( self ):
        return self.montanteAcumulado[-1] - self.capital

    def incrementaDia( self ):
        self.dia = self.dia + self.delta_dias
        self.datas.append( self.dia )




class InvestimentoPreFixado( Investimento ):
    def __init__(self, capital, prazo, taxa, aporte, diaZero=date.today(), name=None, IR=False):
        '''
            taxa - taxa de remuneração AO ANO
        '''
        Investimento.__init__(self, capital, prazo, aporte, diaZero, name, IR)
        self.taxa = self.calculaTaxaEquivalenteMes(taxa)
        
        self.calculaValorFuturo()

    def calculaValorFuturo( self ):
        for i in range(self.prazo):
            M = self.aporte(self.dia)
            self.montante = self.montante*(1+self.taxa)**1 + M*((self.taxa+1)**1 - 1)/self.taxa
            self.montanteAcumulado.append( self.montante )
            self.incrementaDia()
        if self.IR:
            self.montanteAcumulado[-1] *= (1-0.15)

    def calculaTaxaEquivalenteMes( self, taxa ):
        return ((taxa/100. + 1)**(1/12.) - 1)




class InvestimentoPosFixado( Investimento ):
    def __init__(self, capital, prazo, taxa, aporte, indexador, diaZero=date.today(), name=None, IR=False):
        '''
            indexador - indexador ao qual a taxa de juros está atrelada (objeto da classe Indexador)
        '''
        Investimento.__init__(self, capital, prazo, aporte, diaZero, name, IR)
        self.indexador = indexador
        
        self.calculaValorFuturo()

    def calculaValorFuturo( self ):
        for i in range(self.prazo):            
            M = self.aporte(self.dia)
            taxa = self.indexador.calculaTaxa(self.dia)
            self.montante = self.montante*(1+taxa)**1 + M*((taxa+1)**1 - 1)/taxa
            self.montanteAcumulado.append( self.montante )
            self.incrementaDia()
        if self.IR:
            self.montanteAcumulado[-1] *= (1-0.15)


##class Indexador(object):
##    def __

def currencyTicks(x, pos):
    'The two args are the value and tick position'
    locale.setlocale( locale.LC_ALL, '' )
    return locale.currency( x, grouping=True )

def dateTicks(x, pos):
    'The two args are the value and tick position'
    data = date.fromordinal(int(x))
    return data.year


if __name__ == '__main__':
    P = 48000
    M = 4500
    n = 20*12
    taxa = 10.5

    def aporte1( data ):
        if data < date(2021,12,11):
            return 0.
        else:
            return 0.

    c1 = InvestimentoPreFixado(P, n, taxa, aporte1, date.today())
    
    yFormatter = FuncFormatter(currencyTicks)
    xFormatter = FuncFormatter(dateTicks)
    fig, ax = plt.subplots()
    fig.subplots_adjust(left=0.2, bottom=None, right=None, top=None)
    ax.yaxis.set_major_formatter(yFormatter)
    ax.xaxis.set_major_formatter(xFormatter)

    plt.plot(c1.datas, c1.montanteAcumulado, '.-')
    plt.grid(True)
    plt.show()
