import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dfPaises = pd.read_csv('paises.csv', delimiter=';')
dfSpace = pd.read_csv('space.csv', delimiter=';')
dfSpace.columns = dfSpace.columns.str.strip()

# parte 3
# questao 1
iris = sns.load_dataset('iris')
setosa = iris[iris['species'] == 'setosa']
corr = setosa[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].corr()
sns.heatmap(corr, annot=True, fmt='.2f')
plt.show()

# questao 2
titanic = sns.load_dataset('titanic')
sns.histplot(data=titanic, x='age', hue='sex', kde=True)
plt.show()

# questao 3
sns.boxplot(data=titanic, x='class', y='age', hue='sex')
plt.show()

# questao 4
mpg = sns.load_dataset('mpg')
sns.regplot(data=mpg, x='horsepower', y='mpg')
plt.show()

# parte 4
# questao 5
colunas = ['GDP ($ per capita)', 'Literacy (%)', 'Infant mortality (per 1000 births)', 'Phones (per 1000)']
corr_paises = dfPaises[colunas].corr()
sns.heatmap(corr_paises, annot=True, fmt='.2f')
plt.show()

# questao 6
paises_filtrados = dfPaises[dfPaises['Region'].str.contains('LATIN AMER') | dfPaises['Region'].str.contains('WESTERN EUROPE')]
sns.boxplot(data=paises_filtrados, x='Region', y='GDP ($ per capita)')
plt.show()

# questao 7
sns.regplot(data=dfPaises, x='Literacy (%)', y='Infant mortality (per 1000 births)', line_kws={'color': 'red'})
plt.show()

# questao 8
missoes_custo = dfSpace[dfSpace['Cost'] > 0]
sns.boxplot(data=missoes_custo, x='Status Rocket', y='Cost')
plt.show()
