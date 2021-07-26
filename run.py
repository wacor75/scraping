'''
   run:
   Arranca la aplicación del servidor 

   :copyright: Wiliam Arévalo Camacho
   :license: Wiliam Arévalo Camacho
   :author: Wiliam Arévalo Camacho
'''
### Se importan app
from src import app
### arranca  el servidor en el puerto 80
if __name__ == "__main__":
    app.run(debug = True, port = 80)