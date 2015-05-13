# Proyecto-APIS

Autores: Rivas Troncoso, José Rubén - Pérez Rivera, Antonio Miguel.

EXPLICACIÓN DEL PROYECTO:

- Hemos enfocado el uso de las diferentes API's de tal manera que nos basaremos en usar la API de Twitter y la API de Google Drive.


OBJETIVO:

-En primera instancia, realizaremos un 'data mining' conocido ya como la misma minería de datos. Mediante el data mining aplicado sobre Twitter haciendo uso de su API,y pasando por la autenticación claro está, para obtener información de los tweets del siguiente modo:

1.- Información acerca de aquellos tweets realizados según en qué idioma. (Siendo éstos Inglés,Japonés,Francés,Ruso y Español)

2.- Información acerca de aquellos tweets sobre los que se traten temas de algun lenguaje de programación como:
   Ruby, Javascript y Python.
   
- De ello, generaremos mediante el comando en la terminal: $ python twitter_streaming .py > tweet_data.txt 
  un fichero de texto con información de tipo JSON.

-Ésta información será leída posteriormente del fichero de texto mediante otro código en Python del siguiente modo:
 $ python analyze_tweets.py
 
-Con lo cual dicho código se encargará de trabajar con el fichero mencionado, y haciendo uso de modulos de Python como pandas y matplot, generará unas gráficas en formato .png sobre la información obtenida.

-Finalmente el fichero de código en Python, drive_uploader.py, se encargará de hacer la subida de dichas imágenes generadas a Google Drive, haciendo uso de dicha API de Drive, pasando por el tema de la Autenticación hasta acabar realizando la subida.