# import libraries
import pandas as pd
import matplotlib.pyplot as plt

# read cvs file from URL
df = pd.read_csv('https://raw.githubusercontent.com/tangaritas/birds_food/main/pajarines.csv')

# to know data types in dataframe
df.dtypes

# drop irrelevant columns
df.drop(['Unnamed: 6', 'Comidita', 'Costo/g ($)', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13'], axis=1, inplace=True)

# drop rows with missing values 
df.dropna(inplace=True)

# Descriptive statistic
df.describe()

# Group by fruits 
df_fruits = df.groupby('Descripción').sum()

# sum columns
df_fruits.sum()

# mean by month
df_month = df.groupby('Mes').sum()

# Descriptive statistic
df_month.describe()

# Pie chart
df_fruits['Cantidad(g)'].plot.pie(autopct=lambda p:f'{p:.0f} %', figsize=(10, 10), fontsize=12)
plt.title('Lo que han comido las aves en mi ventana en los cinco últimos meses\n', size=16)
plt.show()