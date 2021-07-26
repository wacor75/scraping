'''
   scrap:
      Realiza los procesos de scraping para el negocio

   :copyright: Wiliam Arévalo Camacho
   :license: Wiliam Arévalo Camacho
   :author: Wiliam Arévalo Camacho
'''
### Se importan los plugins necesarios
from bs4 import BeautifulSoup
import requests

def getProducts(url):
    '''
        getProducts: Obtiene los productos que se encuentran el HTML recibido \n
        @params: 
            :url: Dirección de la página web a la que se le hará scrapping
        @return:
            :soup: Contiene la estructura HTML de la página web que se está analizando
    '''
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    products = soup.find_all('div', class_ = 'col-sm-4 col-lg-4 col-md-4')
    resp = []
    for p in products:
        dic = {}
        prd = p.find_next('h4', class_ = "pull-right price")
        if prd:
          dic['price'] = prd.text
        prd = p.find_next('a', class_ = "title")
        if prd:
            dic['object'] = prd.text
        prd = p.find_next('p', class_ = "description")
        if prd:
            dic['description'] = prd.text
        resp.append(dic)
    return resp