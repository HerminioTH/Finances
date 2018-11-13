from Juros import *
from Patrimonio import *
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt

meuPatrimonio = Patrimonio( 48000. )
print meuPatrimonio.capital

prazo = 3*12


def aporte1( data ):
    if data < date(2021, 12, 12):       return 4000
    else:                               return 0


cdi = CDI( 10, 115, 'CDI')

carteira = []
carteira1.append( InvestimentoPreFixado(meuPatrimonio.investeCapital(), prazo, 8.3, aporte1, diaZero=date.today(), name='LCA pre 8,3% a.a.') )
##carteira.append( InvestimentoPreFixado(meuPatrimonio.investeCapital(12000), prazo, 18.51, aporte1, diaZero=date.today(), name='XP Investor 30 FIC FIA 12,51% a.a.') )
##carteira.append( InvestimentoPreFixado(meuPatrimonio.investeCapital(12000), prazo, 10.02, aporte1, diaZero=date.today(), name='CDB pre 10,02% a.a.', IR=True) )
##carteira.append( InvestimentoPosFixado(meuPatrimonio.investeCapital(), prazo, aporte1, cdi, diaZero=date.today(), name='CDB pre 119% CDI', IR=True) )

print meuPatrimonio.capital

for investimento in carteira:
    dividendo = investimento.retornaDividendo()
    meuPatrimonio.recebeDividendo( dividendo )

print meuPatrimonio.capital

plotCenarios( carteira )
