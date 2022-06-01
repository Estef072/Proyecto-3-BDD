import psycopg2

class reporteria:
    def reportar(self):
        connection = psycopg2.connect(user="postgres",
                                            password="3369",
                                            port="5432",
                                            database="proyecto#3")

        cursor = connection.cursor()
        print(" \nPrimera Consulta: TOP 20 peliculas sin terminar \n")
        psql_query = "SELECT * FROM top20_unfinished_movies"
        cursor.execute(psql_query)
        query = cursor.fetchall()
        print(query) 


        print(" \nPrimera Consulta: TOP 5 de los administradores que han modificado más  \n")
        psql_query = "SELECT * FROM top5_administrator"
        cursor.execute(psql_query)
        query = cursor.fetchall()
        print(query) 

        print(" \nPrimera Consulta: TOP 10 de los terminos más buscados  \n")
        psql_query = "SELECT * FROM top10_searches"
        cursor.execute(psql_query)
        query = cursor.fetchall()
        print(query)

r = reporteria()
r.reportar()