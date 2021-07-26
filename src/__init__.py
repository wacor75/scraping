'''
   scraping:
   Aplicación para la realizar scraping en un página web

   :copyright: Wiliam Arévalo Camacho
   :license: Wiliam Arévalo Camacho
   :author: Wiliam Arévalo Camacho

   Made by Wiliam Arévalo Camacho in Medelín - Colombia
   The Software use and distribution is under authorization of Wiliam arévalo Camacho
'''
### Se importan los plugins necesarios
from flask import Flask

### Se instancia la aplicación
app = Flask(__name__)

### Vincular las clases del sistema
from src.service import servicio

### Versión de la aplicación
__version__ = "1.0.0"
