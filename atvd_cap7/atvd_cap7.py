import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

#exerc 1

#airtravel
dfAir = pd.read_csv('airtravel.csv', delimiter=',', index_col='Date', parse_dates=True)
dfAir['Passengers'] = dfAir['Passengers'].astype(float)

dfAir['Passengers'].plot(figsize=(8, 6), title='Passageiros de Linhas Aereas', xlabel='Data', ylabel='Passageiros', x_compat=True)
plt.show()

decomposition_air = seasonal_decompose(dfAir['Passengers'], model='multiplicative')
decomposition_air.plot()
plt.tight_layout()
plt.show()

#respostas airtravel:
#a)serie possui tendencia? Se sim, que tipo?
#Sim possui tendencia crescente com o numero de passageiros subindo de forma constante ao longo dos ano

#b)a serie possui sazonalidade? Se sim, qual o periodo que ela acontece?
#sim, possui sazonalidade anual, ocorre pico no meio do ano durante as ferias de verao no hemisferio norte e quedas na baixa temporada

#c)serie apresenta um ciclo? Se sim, por qual razao?
#nao apresenta ciclo visivel, pois a serie tem apenas 3 anos de dados, pouco tempo para identificar ciclos economicos de longo prazo


#co2_emissions
dfCo2 = pd.read_csv('co2_emissions.csv', delimiter=',', index_col='Year', parse_dates=True)
dfCo2['CO2_Emissions'] = dfCo2['CO2_Emissions'].astype(float)

dfCo2['CO2_Emissions'].plot(figsize=(8, 6), title='Emissoes de CO2', xlabel='Ano', ylabel='Emissoes de CO2', x_compat=True)
plt.show()

decomposition_co2 = seasonal_decompose(dfCo2['CO2_Emissions'], model='additive')
decomposition_co2.plot()
plt.tight_layout()
plt.show()

#respostas co2_emissions:
#a)a serie possui tendencia? Se sim, que tipo?
#sim, possui tendencia decrescente, com as emissoes caindo ao longo dos anos

#b)a serie possui saazonalidade? Se sim, qual o periodo que ela acontece?
#nao possui sazonalidade, pois os dados sao anuais, logo nao ha variacao regular em intervalos curtos, portanto na decomposicao a sazonalidade fica zerada

#c)a serie apresenta um ciclo? se sim, por qual razao?
#sim, apresenta ciclos. Ao longo dos 31 anos ocorrem flutuacoes de medio/longo prazo sem periodo fixo, ligadas a fatores externos como ciclos economicos globais etc.......