#autor Jose Raul Cuaya Hernandez
#importar la funcion de busqueda
from Recetas import Recetas
from bs4 import BeautifulSoup
import requests
URLS = []
postre = Recetas()

def carga_Urls():
    URLS.append("https://www.simplyrecipes.com/frozen-chocolate-covered-bananas-recipe-6455362?print")
    URLS.append("https://www.simplyrecipes.com/chocolate-chip-cookie-cake-recipe-5524897?print")
    URLS.append("https://www.simplyrecipes.com/choco-tacos-recipe-6362474?print")
    URLS.append("https://www.simplyrecipes.com/rice-cake-with-dulce-de-leche-dark-chocolate-recipe-5496988?print")
    URLS.append("https://www.simplyrecipes.com/chocolate-pound-cake-recipe-5218186?print")
    URLS.append("https://www.simplyrecipes.com/recipes/chocolate_covered_pretzels/?print")
    URLS.append("https://www.simplyrecipes.com/chocolate-lava-cake-recipe-5216642?print")


def main():
    carga_Urls()
    
    for i, url in URLS:
        print("Data")
        #hace ua solicitud a la pagina y la combierte en un lxml para
        # poder trabajar con ella  
        result = requests.get(url)
        content = result.text
        soup = BeautifulSoup(content, 'lxml')
        #obtener una trascripcion de toda la pagina
        #transcript = soup.get_text(strip=True, separator = " " )
        #variables
        Id = i
        postre.inserta_recetas(Nombre,Tiempo,Porciones,N_Ingredientes,url)
        Nombre = soup.find('h2',{'class': "main__Title"}).getText()
        Tiempo = soup.find('span',{'class': "meta-text__Time"}).getText()
        Porciones = soup.find('span',{'class': "meta-text_recipe-serving"}).getText()
        N_Ingredientes = soup.find('span',{'class': "section--ingredients_1-0"}).getText()
        postre.inserta_recetas(Id,Nombre,Tiempo,Porciones,N_Ingredientes,url)
        i += 1



main()
print(postre)
