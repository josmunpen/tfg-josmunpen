import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time

def extrae_titular_cuerpo(enlace_articulo):

    articulo = requests.get(enlace_articulo)
    soup = BeautifulSoup(articulo.text, 'lxml')

    titular = soup.find('div', class_='article-header-title col-12').h1
    if titular.span:
        titular.span.decompose()
    titular = titular.text

    parrafos_container = soup.find('div', class_='article-text')
    parrafos = parrafos_container.find_all('p')
    cuerpo = ''
    for p in parrafos:
        cuerpo = cuerpo + ' \n ' + str(p.text)

    return titular, cuerpo

pagina_generica = "https://www.publico.es/page"
sufijo_economia = '/economia-1.html?page='
sufijo_igualdad = '/igualdad.html?settings=%7B"extra"%3A%5B%5D%7D&page='
sufijo_politica = '/politica-1.html?settings=%7B%22pbExtraStyles%22%3A%5B%22first-featured-item%22%5D%7D&page='

pagina_generica = pagina_generica + sufijo_politica

titulares = []
cuerpos = []
it = 400
while it < 600:
    print("Página número " + str(it) + " extraída.")
    pagina = requests.get(pagina_generica + str(it))
    soup = BeautifulSoup(pagina.text, 'lxml')
    articulos_containers = soup.find_all('div', class_='listing-title')
    for art in articulos_containers:
        enlace_articulo = "https://www.publico.es" + art.a['href']
        if 'politica' in enlace_articulo:
            try:
                titular, cuerpo = extrae_titular_cuerpo(enlace_articulo)
                titulares.append(titular)
                cuerpos.append(cuerpo)
            except:
                print("No se puedo extraer el artículo " + enlace_articulo)
    it = it + 1


data_publico = pd.DataFrame(np.array(titulares), np.array(cuerpos))

data_publico.to_csv(r'C:\Users\josemalaptop\codigoScrapin\Scrapping\datos\data_publico_politica_400_600.csv')