import psycopg2
import random
import datetime

class buscar ():
    def busqueda (self):
        dato = input ('Que deseas buscar\n')
        usuario= input("Ingresa tu usuario\n")
        dia =random.randint(1,31)
        mes = random.randint(1,12)
        año = 2022
        hora = random.randint(0,23)
        mins = random.randint(0, 59)
        hora_fecha = datetime.datetime(año, mes, dia,hora, mins)
        datos = [usuario,hora_fecha,dato]
        self.tuplaa = tuple(datos)
        self.connection = psycopg2.connect(dbname ="proyecto#3", user = "postgres", password ="3369")
        self.cursor = self.connection.cursor()
        self.cursor.executemany("insert into busqueda values(%s,%s,	%s)", [self.tuplaa])       
        self.connection.commit ()
        self.connection.close()
        print ("se agregó con exito")

        

c=buscar()
c.busqueda ()