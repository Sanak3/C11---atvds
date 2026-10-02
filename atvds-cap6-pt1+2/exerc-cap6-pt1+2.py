import pandas as pd
import matplotlib.pyplot as plt

dfPaises = pd.read_csv('paises.csv', delimiter=';')
dfSpace = pd.read_csv('space.csv', delimiter=';')

# parte 1
# questao 1
paises_norte = dfPaises[dfPaises['Region'].str.contains('NORTHERN AMERICA')]
plt.plot(paises_norte['Country'], paises_norte['Deathrate'], 'r-', paises_norte['Country'], paises_norte['Birthrate'], 'b--')
plt.show()

# questao 2
missoes_eua = dfSpace[dfSpace['Location'].str.contains('USA')]
missoes_china = dfSpace[dfSpace['Location'].str.contains('China')]
empresas_eua = len(missoes_eua['Company Name'].unique())
empresas_china = len(missoes_china['Company Name'].unique())
plt.bar(['EUA', 'China'], [empresas_eua, empresas_china], color='green')
plt.show()

# questao 3
roscosmos = dfSpace[dfSpace['Company Name'] == 'Roscosmos']
sucesso = len(roscosmos[roscosmos['Status Mission'] == 'Success'])
falha = len(roscosmos) - sucesso
plt.pie(x=[sucesso, falha], labels=['Sucesso', 'Falha'], autopct='%1.1f%%')
plt.show()

# questao 4
falhas = dfSpace[dfSpace['Status Mission'] == 'Failure']
top5_falhas = falhas['Company Name'].value_counts().head(5)
plt.bar(top5_falhas.index, top5_falhas.values, color='red')
plt.show()

# parte 2
# questao 5
paises_latam = dfPaises[dfPaises['Region'].str.contains('LATIN AMER')]
plt.scatter(paises_latam['GDP ($ per capita)'], paises_latam['Literacy (%)'], s=paises_latam['Population'] / 100000)
plt.show()

# questao 6
ativos = len(dfSpace[dfSpace['Status Rocket'] == 'StatusActive'])
aposentados = len(dfSpace[dfSpace['Status Rocket'] == 'StatusRetired'])
plt.pie(x=[ativos, aposentados], labels=['StatusActive', 'StatusRetired'], autopct='%1.1f%%')
plt.show()

# questao 7
paises_europa = dfPaises[dfPaises['Region'].str.contains('WESTERN EUROPE')]
plt.plot(paises_europa['Country'], paises_europa['GDP ($ per capita)'], 'o-r', paises_europa['Country'], paises_europa['Phones (per 1000)'], 's--b')
plt.show()

# questao 8
sucesso = dfSpace[dfSpace['Status Mission'] == 'Success']
top5_sucesso = sucesso['Company Name'].value_counts().head(5)

falha = dfSpace[dfSpace['Status Mission'] == 'Failure']
top5_falha = falha['Company Name'].value_counts().head(5)

plt.subplot(1, 2, 1)
plt.title('Sucesso')
plt.bar(top5_sucesso.index, top5_sucesso.values)

plt.subplot(1, 2, 2)
plt.title('Falha')
plt.bar(top5_falha.index, top5_falha.values)

plt.show()
