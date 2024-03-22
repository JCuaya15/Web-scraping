
from contextlib import nullcontext
from copyreg import constructor
from posixpath import sep
from tracemalloc import start
from unittest import result
from googlesearch import search
from bs4 import BeautifulSoup
import requests
import pymysql

db = pymysql.connect(host='localhost',user='root',password='',database='prueba',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()

ingredientes = []
fichero = open('ingredientes.txt')
lineas = fichero.readlines()
for linea in lineas:
    
    ingredientes.append(linea.rstrip())

#esta variable contiene la busqueda
shg = str(input("Ingresa tu busqueda: "))
sql = "TRUNCATE TABLE datosingre";
cursor.execute(sql)
sql = "TRUNCATE TABLE datosT";
cursor.execute(sql)
#Parametros para la busqueda
tld = "com"
lang = "es"
num = 100
start = 0
stop =num
pause = 2.0
i=1
res = object
busqueda = search(shg, tld=tld, lang=lang, num=num, start=start, stop=stop, pause=pause)

for r in busqueda:
    
    #hace ua solicitud a la pagina y la combierte en un lxml para
    # poder trabajar con ella  
    #print("buscando en la pagina  "+r)
    try:
        result = requests.get(r)
        content = result.text
        soup = BeautifulSoup(content, 'lxml')
        #obtener una trascripcion de toda la pagina
        transcript = soup.get_text(strip=True, separator = " " )
        #busca la palabras clave las cuenta
        #print(transcript)

        
        transcript= transcript.lower()
        
        
        if transcript.count("ingredientes") >0:
            if transcript.count("preparación") >0 or transcript.count("tiempo:") >0:
                ban = True
                ban2 = True
                x=10
                tiempo = ""
                while (ban):
                    mins = str(x)+" mins"
                    minutos = str(x)+" minutos"
                    hrs = str(x)+" hrs"
                    horas = str(x)+" horas"
                    
                    if transcript.count(mins) >0:
                        print ("El tiempo es de "+ str(x)+" mins")   
                        tiempo=mins
                        ban = False
                    elif transcript.count(minutos) >0:
                        print ("El tiempo es de "+ str(x) +" minutos") 
                        tiempo=minutos
                        ban = False
                    elif transcript.count(horas) >0:
                        print ("El tiempo es de "+ str(x)+" horas") 
                        tiempo=horas
                        ban = False
                    elif transcript.count(hrs) >0:
                        print ("El tiempo es de "+ str(x)+" hrs") 
                        tiempo=hrs
                        ban = False
                    x=x+1
                    
                    if x > 1000:
                        print("SIN TIEMPO")
                        tiempo="SIN TIEMPO"
                        ban = False
                        ban2 = False
                    
                    
                if ban2:
                    suma = 0
                    Contingre =0
                    for ingrediente in ingredientes:
                        ingre = ingrediente.split(",")
                        if transcript.count(ingre[0]) > 0:
                            print (r+"  "+ str(ingrediente))
                            suma = suma+int(ingre[1])
                            Contingre = Contingre+1
                            sql = f"INSERT into datosIngre (link,ingrediente,costo) values ('{r}','{ingre[0]}','{ingre[1]}')";        
                            #print(sql)
                            cursor.execute(sql)
                            # Commit your changes in the database
                            db.commit() 
                    sql = f"INSERT into datosT (link,ingredientes,costo,tiempo) values ('{r}','{Contingre}','{suma}','{tiempo}')";
                    #print(sql) 
                    cursor.execute(sql)
                    # Commit your changes in the database
                    db.commit() 
        
       
   
    except:
        print("ERROR en la pagina"+r)
    