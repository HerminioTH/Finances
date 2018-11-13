# -*- coding: cp1252 -*-
from Juros import *
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt

def plotCenarios( investimentos ):
    fig, ax = plt.subplots()
    yFormatter = FuncFormatter(currencyTicks)
    xFormatter = FuncFormatter(dateTicks)
    ax.yaxis.set_major_formatter(yFormatter)
    ax.xaxis.set_major_formatter(xFormatter)
    fig.subplots_adjust(left=0.2, bottom=None, right=None, top=None)

    for c in investimentos:
        plt.plot(c.datas, c.montanteAcumulado, '.-', label=c.name)

    plt.grid(True)
    plt.legend(loc=0)
    plt.show()

class Patrimonio(object):
    def __init__( self, capital ):
        self.capital = capital

    def investeMontante( self, montante ):
        self.capital -= montante
        if self.capital >= 0:
            return montante
        else:
            print 'Montante excede o patrimonio.'
            return 0

    def recebeDividendo( self, dividendo ):
        self.capital += dividendo

class Salario(object):
    def __init__(self, salario):
        self.salario

    def debito(self, valor):
        self.salario -= valor
        if self.salario >= 0:
            return valor



meuPatrimonio = Patrimonio( 48000. )
prazo = 10*12

investimentos = []

def aporte1( dia ):
    if dia < date(2021, 12, 12):        return 3000
    else:                               return 2000
investimentos.append( Investimento(meuPatrimonio.investeMontante(46000), prazo, 8.3, aporte1, diaZero=date.today(), name='LCA pre 8,3% a.a.') )

def aporte2( dia ):
    if dia < date(2021, 11, 12):        return 1000
    else:                               return 2000.
investimentos.append( Investimento(meuPatrimonio.investeMontante(2000), prazo, 12.51, aporte2, diaZero=date.today(), name='XP Investor 30 FIC FIA 18,51% a.a.') )



for investimento in investimentos:
    meuPatrimonio.recebeDividendo( investimento.retornaDividendo() )

print meuPatrimonio.capital

plotCenarios( investimentos )



