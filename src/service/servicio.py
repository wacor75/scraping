'''
   servicio:
      Administra los servicios que realizan el scraping de una pagina

   :copyright: Wiliam Arévalo Camacho
   :license: Wiliam Arévalo Camacho
   :author: Wiliam Arévalo Camacho
'''
### Se importan los plugins necesarios
from flask import jsonify, request
from src import app
from src.core import scrap
### Establece la URL que se utilizara para hacer el scraping
dir = "https://webscraper.io/test-sites/e-commerce/scroll"

@app.route('/')
def inicio():
   '''
      inicio: Presenta la información del programa \n
   '''
   print("In inicio \n")
   texto = scrap.getProducts(dir)
   return jsonify({'products': texto})

