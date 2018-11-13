# -*- coding: cp1252 -*-
from Juros import *
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt

def plotCenarios( cenarios ):
    fig, ax = plt.subplots()
    yFormatter = FuncFormatter(currencyTicks)
    xFormatter = FuncFormatter(dateTicks)
    ax.yaxis.set_major_formatter(yFormatter)
    ax.xaxis.set_major_formatter(xFormatter)
    fig.subplots_adjust(left=0.2, bottom=None, right=None, top=None)

    for c in cenarios:
        plt.plot(c.datas, c.montanteAcumulado, '.-', label=c.name)

    plt.grid(True)
    plt.legend(loc=0)
    plt.show()
    


P = 48000.
n = 5*12

cenarios = []

def aporte1( dia ):
    if dia < date(2021, 11, 12):
        return 4000
    else:
        return 5000
cenarios.append( Cenario(P, n, 6.999, aporte1, diaZero=date.today(), name='Poupanca - 2017') )

def aporte2( dia ):
    if dia < date(2021, 11, 12):
        return 4000
    else:
        return 5000.
cenarios.append( Cenario(P, n, 10.02, aporte2, diaZero=date.today(), name='CDB pre 10,02% a.a.') )

def aporte3( dia ):
    if dia < date(2021, 11, 12):
        return 4000
    else:
        return 5000.
cenarios.append( Cenario(P, n, 8.3, aporte3, diaZero=date.today(), name='LCA pre 8,3% a.a.') )

def aporte4( dia ):
    if dia < date(2021, 11, 12):
        return 4000
    else:
        return 5000.
cenarios.append( Cenario(P, n, 18.51, aporte4, diaZero=date.today(), name='XP Investor 30 FIC FIA 18,51% a.a.') )

def aporte5( dia ):
    if dia < date(2021, 11, 12):
        return 8000
    else:
        return 0.
cenarios.append( Cenario(P, n, 18.51, aporte5, diaZero=date.today(), name='XP Investor 30 FIC FIA 18,51% a.a.') )



plotCenarios( cenarios )



