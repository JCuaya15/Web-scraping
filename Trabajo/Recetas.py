import mysql.connector


class Recetas:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="12345678", database="bd_recetas")

    def __str__(self):
        datos=self.consulta_recetas()
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
    
    def consulta_recetas(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM recetas")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def consulta_receta(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM c WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos

    def inserta_recetas(self,Nombre, Tiempo, Porciones, N_Ingredientes, Url):
        cur = self.cnn.cursor()
        sql='''INSERT INTO recetas (Nombre, Tiempo, Porciones, N_Ingredientes, Url) 
        VALUES('{}', '{}', '{}', '{}')'''.format(Nombre, Tiempo, Porciones, N_Ingredientes, Url)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_recetas(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM recetas WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_receta(self,Id,Nombre, Tiempo, Porciones, N_Ingredientes, Url):
        cur = self.cnn.cursor()
        sql='''UPDATE countries SET ISO3='{}', CountryName='{}', Capital='{}',
        CurrencyCode='{}' WHERE Id={}'''.format(Nombre, Tiempo, Porciones, N_Ingredientes, Url,Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
