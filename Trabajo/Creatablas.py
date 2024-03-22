from itertools import count
from statistics import median
import string
import pandas as pd
import matplotlib.pyplot as plt

from sqlalchemy import create_engine
hostname="localhost"
dbname = "bd_recetas"
uname="root" 
pwd="12345678"
tablename="datost"
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname,user=uname,pw=pwd))
df = pd.read_sql(tablename, engine)

df.to_csv('data.csv')
#df['tiempo'] = df['tiempo'].astype('float64')



def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
    return num

salir = False
opcion = 0

while not salir:

    print ("1. Mostrar menor costo")
    print ("2. Mostrar menor tiempo")
    print ("3. Mostrar menor uso de ingredientes")
    print ("4. Graficas")
    print ("5. Estadisticas")
    print ("6. Salir")
    print ("Elige una opcion")

    opcion = pedirNumeroEntero()

    if opcion == 1:
        print ("**Mostrar menor costo**")
        dfcosto = df.sort_values('costo')
        print("Nombre: "+dfcosto.iloc[0,6])
        print("Costo: "+dfcosto.iloc[0,3])
        print("Numero de ingredientes: "+dfcosto.iloc[0,2])
        print("Tiempo: "+dfcosto.iloc[0,4])
        print("Porciones: "+dfcosto.iloc[0,5])
        print("Link: "+dfcosto.iloc[0,1])
    elif opcion == 2:
        print ("**Mostrar menor tiempo**")
        dftiempo = df.sort_values('tiempo')
        print("Nombre: "+dftiempo.iloc[0,6])
        print("Costo: "+dftiempo.iloc[0,3])
        print("Numero de ingredientes: "+dftiempo.iloc[0,2])
        print("Tiempo: "+dftiempo.iloc[0,4])
        print("Porciones: "+dftiempo.iloc[0,5])
        print("Link: "+dftiempo.iloc[0,1])
    elif opcion == 3:
        print("Mostrar menor uso de ingredientes")
        dfingredietes = df.sort_values('ingredientes')
        print("Nombre: "+dfingredietes.iloc[0,6])
        print("Costo: "+dfingredietes.iloc[0,3])
        print("Numero de ingredientes: "+dfingredietes.iloc[0,2])
        print("Tiempo: "+dfingredietes.iloc[0,4])
        print("Porciones: "+dfingredietes.iloc[0,5])
        print("Link: "+dfingredietes.iloc[0,1])
    elif opcion == 4:
        print("Graficas")
        df['costo'] = df['costo'].astype(float)
        df['ingredientes'] = df['ingredientes'].astype(float)
        df['tiempo'] = df['tiempo'].str.replace('minutos','').astype(float)
        #Grafica ingredientes
        X = list(df.iloc[:, 0])
        Y = list(df.iloc[:, 2])
        # Plot the data using bar() method
        plt.bar(X, Y, color='g')
        plt.title("Cuantos Ingredientes necesita")  
        plt.xlabel("ID de la receta", fontsize=10)
        plt.ylabel("Numero de ingredientes", fontsize=10)
        plt.show()
        #Grafica Tiempo
        print("**********")
        X = list(df.iloc[:, 0])
        Y = list(df.iloc[:, 4])
        # Plot the data using bar() method
        plt.plot(X, Y, 'o:r', ms = 20, mec = 'r', mfc = 'r')
        plt.title("Tiempo de elaboracion")  
        plt.xlabel("Nombre de la receta", fontsize=10)
        plt.ylabel("Tiempo", fontsize=10)
        plt.show()
        #Grafica costo
        #dfcosto = df.sort_values('costo')
        print("**********")
        X= list(df.iloc[:, 0])
        Y = list(df.iloc[:, 3])
        # Plot the data using bar() method
        plt.bar(X, Y, color='b')
        #print(dfcosto.head)
        plt.title("Costo por Receta")  
        plt.xlabel("Nombre de la receta", fontsize=10)
        plt.ylabel("Costo", fontsize=10)
        plt.show()
        #Grafica perosonas
        print("**********")
        X = list(df.iloc[:, 0])
        Y = list(df.iloc[:, 5])
        # Plot the data using bar() method
        plt.bar(X, Y, color='g')
        plt.title("Numero de Personas")  
        plt.xlabel("Nombre de la receta", fontsize=10)
        plt.ylabel("Personas", fontsize=10)
        plt.show()
    elif opcion == 5:
        print("Estadisticas")
        des_Ingredientes = df['ingredientes'].describe()
        des_Costo = df['costo'].describe()
        des_time = df['tiempo'].describe()
        print("**Ingredientes**")
        print(des_Ingredientes)
        print("**Costo**")
        print(des_Costo)
        print("**Tiempo**")
        print(des_time)
    elif opcion == 6:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 6  ")
print ("Fin")
