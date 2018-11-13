# -*- coding: cp1252 -*-
import locale
from datetime import date, timedelta
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np

class Investimento(object):
    def __init__( self, capital, nAportes, taxa, funAportes, diaZero=date.today(), name=None, IR=False ):
        ''' P - aporte inicial
            M - função que calcula o aporte mensal
            n - número de períodos em mêses
            i - taxa de juros em %
            day_0 - data de início
        '''
        self.capital = capital
        self.montante = capital
        self.funAportes = funAportes
        self.nAportes = nAportes
        self.diaZero = diaZero
        self.dia = diaZero
        self.delta_dias = timedelta(30)                     # mensal
        self.taxa = self.calculaTaxaEquivalenteMes(taxa)
        self.name = name
        self.IR = IR

        self.montanteAcumulado = []
        self.datas = []
        self.calculaValorFuturo()

    def retornaDividendo( self ):
        return self.montanteAcumulado[-1] - self.capital

    def calculaTaxaEquivalenteMes( self, taxa ):
        return ((taxa/100. + 1)**(1/12.) - 1)

    def incrementaDia( self ):
        self.dia = self.dia + self.delta_dias
        self.datas.append( self.dia )
        

    def calculaValorFuturo( self ):
        for i in range(self.nAportes):
            M = self.funAportes(self.dia)
            self.montante = self.montante*(1+self.taxa)**1 + M*((self.taxa+1)**1 - 1)/self.taxa
            self.montanteAcumulado.append( self.montante )
            self.incrementaDia()
        if self.IR:
            self.montanteAcumulado[-1] *= (1-0.15)

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
    n = 6
    taxa = 0.65

    def aporte1( dia ):
        if dia < date(2021,12,11):
            return 4500.
        else:
            return 4500.

    c1 = Investimento(P, n, taxa, aporte1)
    
    yFormatter = FuncFormatter(currencyTicks)
    xFormatter = FuncFormatter(dateTicks)
    fig, ax = plt.subplots()
    fig.subplots_adjust(left=0.2, bottom=None, right=None, top=None)
    ax.yaxis.set_major_formatter(yFormatter)
    ax.xaxis.set_major_formatter(xFormatter)

    plt.plot(c1.datas, c1.montanteAcumulado, '-o')
    plt.grid(True)
    plt.show()
