from numpy import integer
import psycopg2

class eliminar ():
    def eliminar (self,dato):
        if dato == 1 : 
            pelicula = input("Ingrese el nombre de la pelicula que  desea eliminar")
            id = int(input ("ingrese el id de la pelicula"))
            datos = [pelicula]
            self.tuplaa = tuple(datos)
            self.connection = psycopg2.connect(dbname ="proyecto#3", user = "postgres", password ="3369")
            self.cursor = self.connection.cursor()
            self.cursor.execute("DELETE FROM peliculas WHERE  titulo =%s  ",self.tuplaa)      
            self.connection.commit ()
            self.connection.close()
        
c=eliminar()
c.eliminar (1)