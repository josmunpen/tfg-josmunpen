import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def extrae_titular_cuerpo(enlace_articulo):

    articulo = requests.get(enlace_articulo)
    soup = BeautifulSoup(articulo.text, 'lxml')
    

    if soup.find('h1', class_='headline | font--primary headline'):
        titular = soup.find('h1', class_='headline | font--primary headline').span.string
    elif soup.find('div', class_='opinion-title'):
        titular = soup.find('div', class_='opinion-title').string
    else:
        titular = 'NaN'

    container = soup.find(class_='article__body-container')
    section = container.section
    parrafos = section.find_all("p")
    cuerpo = ""
    for parrafo in parrafos:
        if parrafo.string:
            cuerpo = cuerpo + " \n " + str(parrafo.string)
        else:
            cuerpo = cuerpo + str(parrafo.text)

    return titular, cuerpo

pagina_generica = "https://www.larazon.es/"

sufijo_espana = 'espana/'
sufijo_cultura = 'cultura/'

titulares = []
cuerpos = []
it = 400 
while it < 800:
    print("Página número " + str(it) + " extraída.")
    pagina = requests.get(pagina_generica + sufijo_espana + str(it))
    soup = BeautifulSoup(pagina.text, 'lxml')
    articulos = soup.find_all('article', class_='card grid--has-3-col')
    for articulo in articulos:
        enlace_articulo = articulo.h3.a['href']
        try:
            titular, cuerpo = extrae_titular_cuerpo(enlace_articulo)
            titulares.append(titular)
            cuerpos.append(cuerpo)
        except:
            print("No se pudo guardar el artículo.")

    it = it + 1

data_larazon_espana = pd.DataFrame(np.array(titulares), np.array(cuerpos))

data_larazon_espana.to_csv(r'C:\scrapin\datos\data_larazon_cultura_400_800.csv')