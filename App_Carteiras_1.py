from Juros import *
from Patrimonio import *
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import locale
locale.setlocale( locale.LC_ALL, '' )


mp = Patrimonio( 48000. )
print( locale.currency( mp.capital, grouping=True ) )


capital = 48000

prazo = 8*12

cdi = CDI( 10, 121, 'CDI')
ipca = IPCA( 5.5, 5.2, 'IPCA')

carteira = []

def aporte1( data ):
    if data <= date(2019, 6, 1):       							return 1000
    elif date(2019, 6, 1) < data and data < date(2021, 6, 1): 	return 1000
    else:                               						return 800
carteira.append( InvestimentoPreFixado(mp.investeCapital(15000), prazo, 8.3, aporte1, diaZero=date.today(), name='LCA pre 8,3% a.a.') )

def aporte1( data ):
    if data <= date(2019, 6, 1):       							return 1000
    elif date(2019, 6, 1) < data and data < date(2021, 6, 1): 	return 1000
    else:                               						return 800
carteira.append( InvestimentoPreFixado(mp.investeCapital(5000), prazo, 12.51, aporte1, diaZero=date.today(), name='XP Investor 30 FIC FIA 12,51% a.a.', IR=True) )

def aporte1( data ):
    if data <= date(2019, 6, 1):       							return 1000
    elif date(2019, 6, 1) < data and data < date(2021, 6, 1): 	return 1000
    else:                               						return 800
carteira.append( InvestimentoPreFixado(mp.investeCapital(10000), prazo, 10.02, aporte1, diaZero=date.today(), name='CDB pre 10,02% a.a.', IR=True) )

def aporte1( data ):
    if data <= date(2019, 6, 1):       							return 1000
    elif date(2019, 6, 1) < data and data < date(2021, 6, 1): 	return 1000
    else:                               						return 800
carteira.append( InvestimentoPosFixado(mp.investeCapital(10000), prazo, aporte1, cdi, diaZero=date.today(), name='CDB pos 121% CDI', IR=True) )

def aporte1( data ):
    if data <= date(2019, 6, 1):       							return 1000
    elif date(2019, 6, 1) < data and data < date(2021, 6, 1): 	return 1000
    else:                               						return 800
carteira.append( InvestimentoPosFixado(mp.investeCapital(8000), prazo, aporte1, ipca, diaZero=date.today(), name='Tesouro Direto', IR=True) )


print( locale.currency( mp.capital, grouping=True ) )

for investimento in carteira:
    dividendo = investimento.retornaDividendo()
    mp.recebeDividendo( dividendo )

print( locale.currency( mp.capital, grouping=True ) )

plotCenarios( carteira )


