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
        self.carteira = []

    def investeCapital( self, valor=None ):
        if valor == None:
            valor = self.capital
            self.capital = 0
            return valor
        else:
            self.capital -= valor
            if self.capital >= 0:
                return valor
            else:
                print 'Valor excede o patrimonio.'
                return 0

    def recebeDividendo( self, dividendo ):
        self.capital += dividendo


##class Salario(object):
##    def __init__(self, salario, data):
##        self.salario = salario
##        self.vencimento = data.day     # Dia de recebimento
##
##class ContaCorrente(object):
##    def __init__(self, salarioMensal, data):
##        self.salario = salarioMensal
##        self.saldo = 0
##
##    def calculaSaldo(self, dia):
##        
##        
##    def debito(self, valor, dia):
##        self.saldo -= valor
##        if self.salario >= 0:
##            return valor


if __name__ == '__main__':
    meuPatrimonio = Patrimonio( 48000. )

    prazo = 10*12

    carteira = []

    def aporte1( data ):
        if data < date(2021, 12, 12):       return 1500
        else:                               return 2000
    carteira.append( InvestimentoPreFixado(meuPatrimonio.investeCapital(28000), prazo, 8.3, aporte1, diaZero=date.today(), name='LCA pre 8,3% a.a.') )

    def aporte2( data ):
        if data < date(2021, 11, 12):       return 1000
        else:                               return 2000.
    carteira.append( InvestimentoPreFixado(meuPatrimonio.investeCapital(2000), prazo, 12.51, aporte2, diaZero=date.today(), name='XP Investor 30 FIC FIA 12,51% a.a.') )


    carteira.append( InvestimentoPreFixado(meuPatrimonio.investeCapital(), prazo, 10.02, aporte1, diaZero=date.today(), name='CDB pre 10,02% a.a.', IR=True) )

    print meuPatrimonio.capital

    for investimento in carteira:
        meuPatrimonio.recebeDividendo( investimento.retornaDividendo() )

    print meuPatrimonio.capital

    plotCenarios( carteira )



