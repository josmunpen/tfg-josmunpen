import pandas as pd

df1 = pd.read_csv(r'C:\Users\josemalaptop\codigoScrapin\Scrapping\datos\data_publico_economia_2_100.csv')

df2 = pd.read_csv(r'C:\Users\josemalaptop\codigoScrapin\Scrapping\datos\data_publico_economia_100_200.csv')

df3 = pd.read_csv(r'C:\Users\josemalaptop\codigoScrapin\Scrapping\datos\data_publico_igualdad_2_60.csv')

df4 = pd.read_csv(r'C:\Users\josemalaptop\codigoScrapin\Scrapping\datos\data_publico_politica_2_400.csv')


print("Datos de economía de las páginas 1 a 100:")
print(df1.shape)
print(df1.head)

print("Datos de economía de las páginas 100 a 200:")
print(df2.shape)
print(df2.head())

print("Datos de igualdad de las páginas 1 a 60:")
print(df3.shape)
print(df3.head())

print("Datos de política de las páginas 1 a 400:")
print(df4.shape)
print(df4.head())

datos_unidos = pd.concat([df1,df2,df3,df4])


print("Datos unidos")
print(datos_unidos.shape) # (27052, 2)
print(datos_unidos.head())

datos_unidos.to_csv(r'C:\Users\josemalaptop\codigoScrapin\Scrapping\datos\data_publico_unidos.csv')