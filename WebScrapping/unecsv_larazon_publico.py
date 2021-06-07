import pandas as pd

df1 = pd.read_csv(r'C:\Users\josemalaptop\codigoScrapin\Scrapping\datos\unidos_prepro\data_larazon_unidos_prepro_2.csv')

df2 = pd.read_csv(r'C:\Users\josemalaptop\codigoScrapin\Scrapping\datos\unidos_prepro\data_publico_unidos_prepro_2.csv')

print("Datos de La Razón:")
print(df1.shape)
print(df1.head)

print("Datos de Público:")
print(df2.shape)
print(df2.head())

datos_unidos = pd.concat([df1,df2])


print("Datos unidos")
print(datos_unidos.shape) # (58525, 4)
print(datos_unidos.head())

datos_unidos.to_csv(r'C:\Users\josemalaptop\codigoScrapin\Scrapping\datos\unidos_prepro\data_larazon_publico.csv')