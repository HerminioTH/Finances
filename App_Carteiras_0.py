from Juros import *
from Patrimonio import *
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt

meuPatrimonio = Patrimonio( 48000. )
print meuPatrimonio.capital

capital = 48000

prazo = 15*12


def aporte1( data ):
    if data < date(2021, 12, 12):       return 4000
    else:                               return 4000


cdi = CDI( 10, 115, 'CDI')
ipca = IPCA( 4, 5.2, 'IPCA')

carteira = []
carteira.append( InvestimentoPreFixado(capital, prazo, 8.3, aporte1, diaZero=date.today(), name='LCA pre 8,3% a.a.') )
carteira.append( InvestimentoPreFixado(capital, prazo, 12.51, aporte1, diaZero=date.today(), name='XP Investor 30 FIC FIA 12,51% a.a.', IR=True) )
carteira.append( InvestimentoPreFixado(capital, prazo, 10.02, aporte1, diaZero=date.today(), name='CDB pre 10,02% a.a.', IR=True) )
carteira.append( InvestimentoPosFixado(capital, prazo, aporte1, cdi, diaZero=date.today(), name='CDB pos 119% CDI', IR=True) )
carteira.append( InvestimentoPosFixado(capital, prazo, aporte1, ipca, diaZero=date.today(), name='Tesouro Direto', IR=True) )

print meuPatrimonio.capital

for investimento in carteira:
    dividendo = investimento.retornaDividendo()
    meuPatrimonio.recebeDividendo( dividendo )

print meuPatrimonio.capital

plotCenarios( carteira )


