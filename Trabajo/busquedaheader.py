from sqlite3 import Time
from bs4 import BeautifulSoup
from random import randint
from time import sleep
from googlesearch import search
import pymysql
import requests

db = pymysql.connect(host='localhost',user='root',password='12345678',database='bd_recetas',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()


ingredientes = []
fichero = open('ingredientes.txt')
lineas = fichero.readlines()
for linea in lineas:
    
    ingredientes.append(linea.rstrip())

#esta variable contiene la busqueda
query = str(input("Ingresa tu busqueda: "))

sql = "TRUNCATE TABLE datosingre";
cursor.execute(sql)
sql = "TRUNCATE TABLE datosT";
cursor.execute(sql)

#Parametros para la busqueda
busqueda = search(query, tld = 'com', lang = 'es', num = 50, start = 0, stop = 50, pause = 2.0)

def main():
    i=1
    for r in busqueda:
        #hace ua solicitud a la pagina y la combierte en un lxml para
        # poder trabajar con ella
        try:  
            result = requests.get(r)
            content = result.text
            soup = BeautifulSoup(content, 'html.parser')
            #obtener una trascripcion de toda la pagina
            #print(soup.title.string)
            transcript = soup.get_text(strip=True, separator = " " )
            #busca la palabras clave las cuenta
            transcript= transcript.lower()
            
            #print(r)
            if transcript.count("ingredientes") >0:
                if transcript.count("preparación") >0 or transcript.count("tiempo:") >0:
                    ban = True
                    ban2 = True
                    x=10
                    tiempo = ""
                    while (ban):
                        ingre = []
                        mins = str(x)+" mins"
                        minutos = str(x)+" minutos"
                        hrs = str(x)+" hrs"
                        horas = str(x)+" horas"

                        if transcript.count(mins) >0:
                            #print ("El tiempo es de "+ str(x)+" mins")   
                            tiempo=mins
                            ban = False
                        elif transcript.count(minutos) >0:
                            #print ("El tiempo es de "+ str(x) +" minutos") 
                            tiempo=minutos
                            ban = False
                        elif transcript.count(horas) >0:
                            #print ("El tiempo es de "+ str(x)+" horas") 
                            tiempo=horas
                            ban = False
                        elif transcript.count(hrs) >0:
                            #print ("El tiempo es de "+ str(x)+" hrs") 
                            tiempo=hrs
                            ban = False
                        x=x+1
                        if x > 1000:
                            #print("SIN TIEMPO")
                            tiempo="SIN TIEMPO"
                            ban = False
                            ban2 = False
                        

                    if ban2:
                        suma = 0
                        Contingre =0
                        
                        for ingrediente in ingredientes:
                            ingre = ingrediente.split(",")
                            if transcript.count(ingre[0]) > 0:
                                print ("  "+ str(ingrediente))
                                suma = suma+int(ingre[1])
                                Contingre = Contingre+1
                                sql = f"INSERT into datosIngre (link,ingrediente,costo) values ('{r}','{ingre[0]}','{ingre[1]}')";
                                cursor.execute(sql)
                                db.commit();
                        if tiempo !="SIN TIEMPO":
                            personas =randint(4,8)
                            name =soup.title.string
                            sql = f"INSERT into datosT (link,ingredientes,costo,tiempo,personas,name) values ('{r}','{Contingre}','{suma}','{tiempo}','{personas}','{name}')";
                            print(soup.title.string)
                            print(tiempo)
                            print(suma)
                            print(Contingre)
                            print(personas)
                            print(r)
                            cursor.execute(sql)
                            db.commit()
            sleep(randint(1,5))

        except:
            sleep(1)
            #print ("")

main()

