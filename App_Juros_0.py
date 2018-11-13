# -*- coding: cp1252 -*-
from Juros import *
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt


P = 48000.
n = 120
T = n
taxa = 6.55/12

cenarios = []

def aporte1( periodo ): return 4000.
cenarios.append( Cenario(P, n, taxa, aporte1, 'Cenario 1') )

def aporte2( periodo ):
    if periodo < T:
        return 6000
    else:
        return 2000
cenarios.append( Cenario(P, n, taxa, aporte2, 'Cenario 2') )

def aporte3( periodo ):
    if periodo < T:
        return 2000
    else:
        return 6000
cenarios.append( Cenario(P, n, taxa, aporte3, 'Cenario 3') )



formatter = FuncFormatter(millions)
fig, ax = plt.subplots()
fig.subplots_adjust(left=0.2, bottom=None, right=None, top=None)
ax.yaxis.set_major_formatter(formatter)

for c in cenarios:
    plt.plot(c.periodos, c.montanteAcumulado, '.-', label=c.name)

plt.grid(True)
plt.legend(loc=0)
plt.show()



