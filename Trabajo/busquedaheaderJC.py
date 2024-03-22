#autor Jose Raul Cuaya Hernandez
#importar la funcion de busqueda
from Recetas import Recetas
from bs4 import BeautifulSoup
import requests
URLS = []
postre = Recetas()

def carga_Urls():
    URLS.append("https://www.simplyrecipes.com/frozen-chocolate-covered-bananas-recipe-6455362?print")


def main():
    carga_Urls()
    
    for url in URLS:
        print("Data")
        #hace ua solicitud a la pagina y la combierte en un lxml para
        # poder trabajar con ella  
        result = requests.get(url)
        content = result.text
        soup = BeautifulSoup(content, 'lxml')
        print(soup.prettify())
        #obtener una trascripcion de toda la pagina
        #transcript = soup.get_text(strip=True, separator = " " )
        #variables




main()
