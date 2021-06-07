import pandas as pd

df1 = pd.read_csv(r'C:\Users\josemalaptop\codigoScrapin\Scrapping\datos\data_larazon_espana_1_440.csv')

df2 = pd.read_csv(r'C:\Users\josemalaptop\codigoScrapin\Scrapping\datos\data_larazon_espana_450_600.csv')

df3 = pd.read_csv(r'C:\Users\josemalaptop\codigoScrapin\Scrapping\datos\data_larazon_espana_600_800.csv')

df4 = pd.read_csv(r'C:\Users\josemalaptop\codigoScrapin\Scrapping\datos\data_larazon_espana_800_1200.csv')

df5 = pd.read_csv(r'C:\Users\josemalaptop\codigoScrapin\Scrapping\datos\data_larazon_espana_1200_1600.csv')

df6 = pd.read_csv(r'C:\Users\josemalaptop\codigoScrapin\Scrapping\datos\data_larazon_espana_1600_1900.csv')

df7 = pd.read_csv(r'C:\Users\josemalaptop\codigoScrapin\Scrapping\datos\data_larazon_cultura_2_400.csv')

df8 = pd.read_csv(r'C:\Users\josemalaptop\codigoScrapin\Scrapping\datos\data_larazon_cultura_400_800.csv')



print("Datos de las páginas 1 a 440:")
print(df1.shape)
print(df1.head)

print("Datos de las páginas 450 a 600:")
print(df2.shape)
print(df2.head())

print("Datos de las páginas 600 a 800:")
print(df3.shape)
print(df3.head())

print("Datos de las páginas 800 a 1200:")
print(df4.shape)
print(df4.head())

print("Datos de las páginas 1200 a 1600:")
print(df5.shape)
print(df5.head())

print("Datos de las páginas 1600 a 1900:")
print(df6.shape)
print(df6.head())

print("Datos de cultura de las páginas 2 a 400:")
print(df7.shape)
print(df7.head())

print("Datos de cultura de las páginas 400 a 800:")
print(df8.shape)
print(df8.head())


datos_unidos = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8])


print("Datos unidos")
print(datos_unidos.shape) # (31757, 2)
print(datos_unidos.head())

datos_unidos.to_csv(r'C:\Users\josemalaptop\codigoScrapin\Scrapping\datos\data_larazon_unidos.csv')