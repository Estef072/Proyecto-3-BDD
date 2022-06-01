
import psycopg2 
from hashlib import sha256
import random

class paginaP:
    def principal (self):
        ejecucion = True
        while (ejecucion ==True):
            print(" \nA que tipo de usuario perteneces:")
            tipoC = input ("Administrador o usuario estandar  \n")
            if tipoC == "administrador":
                usuario = input("ingrese su usuario \n")
                con = input ("ingrese su contraseña \n")
                contra = "administrador"
                datos = [usuario,con,contra]
                self.tuplas = tuple(datos)
                self.connection = psycopg2.connect(dbname ="proyecto#3", user = "postgres", password ="3369")
                self.cursor = self.connection.cursor()
                self.cursor.execute("SELECT* FROM usuarios WHERE usuario=%s and password=%s and tipo_usuarios=%s",self.tuplas)        
                row =self.cursor.fetchone()
                print (row)
                if row == None:
                    ejecucion  = True
                    print(" __________")
                    print("|   Error\n|")
                    print("|__________|")
                    print("no eres un usuario administrador")
                    while (ejecucion == True):
                        usuario = input("ingrese su usuario \n")
                        con = input ("ingrese su contraseña \n")
                        contra = "administrador"
                        datos = [usuario,contra,con]
                        self.tuplas = tuple(datos)
                        self.connection = psycopg2.connect(dbname ="proyecto#3", user = "postgres", password ="3369")
                        self.cursor = self.connection.cursor()
                        self.cursor.execute("SELECT* FROM usuarios WHERE usuario=%s and tipo_usuarios=%s  and password = %s",self.tuplas)
                        row =self.cursor.fetchone()

                        if row == None:
                            print(" __________")
                            print("|   Error  |")
                            print("|__________|")
                            print("no eres un usuario estandar")
                        else:
                            self.connection.commit ()
                            self.connection.close()
                            print(" ______________________")
                            print("|  Bienvenido          |")
                            print("|______________________|")
                            print("Menú de operaciones")
                            print("1.Mantenimiendo de administradores")
                            print("2. Simulaciones")
                            print("3. Busqueda")
                            print("4. Opciones avanzadas")
                            print("5. Reporteria")
                            dato = int (input("Selecciona una opción: \n"))
                            if dato == 1:
                                import Crear
                                print ("administrador creado con éxito")
                            elif dato == 2:
                                import simulacion
                            elif dato == 3:
                                import buscar
                            elif dato == 4:
                                print ("1.Eliminar")
                                print ("2.Agregar")
                                print ("3.Modificar")
                                dato2  = int(input ("Ingrese la opcion que desea:\n"))
                                if dato2 == 1:
                                    print ("1. Usuarios")
                                    print ("2. Perfiles")
                                    print(" 3. Peliculas")
                                    print ("4. Directores")
                                    print ("5. Anuncios")
                                    index = int(input ("Seleccione una opcion"))
                                    if index == 1:
                                        usuario = input("Ingrese el nombre del usuario que  desea eliminar\n")
                                        datos = [usuario]
                                        self.tuplaa = tuple(datos)
                                        self.connection = psycopg2.connect(dbname ="proyecto#3", user = "postgres", password ="3369")
                                        self.cursor = self.connection.cursor()
                                        self.cursor.execute("DELETE FROM usuarios WHERE  usuario =%s  ",self.tuplaa)      
                                        self.connection.commit ()
                                        self.connection.close()
                                    elif index == 2:
                                        perfil = input("Ingrese el nombre del perfil que  desea eliminar\n")
                                        datos = [perfil]
                                        self.tuplaa = tuple(datos)
                                        self.connection = psycopg2.connect(dbname ="proyecto#3", user = "postgres", password ="3369")
                                        self.cursor = self.connection.cursor()
                                        self.cursor.execute("DELETE FROM perfiles WHERE  nombre_perfil =%s  ",self.tuplaa)      
                                        self.connection.commit ()
                                        self.connection.close()
                                    elif index == 3:
                                        pelicula = input("Ingrese el nombre de la pelicula que  desea eliminar\n")
                                        datos = [pelicula]
                                        self.tuplaa = tuple(datos)
                                        self.connection = psycopg2.connect(dbname ="proyecto#3", user = "postgres", password ="3369")
                                        self.cursor = self.connection.cursor()
                                        self.cursor.execute("DELETE FROM peliculas WHERE  titulo =%s  ",self.tuplaa)      
                                        self.connection.commit ()
                                        self.connection.close()
                                    elif index == 4:
                                        director = input("Ingrese el nombre del director que  desea eliminar\n")
                                        datos = [director]
                                        self.tuplaa = tuple(datos)
                                        self.connection = psycopg2.connect(dbname ="proyecto#3", user = "postgres", password ="3369")
                                        self.cursor = self.connection.cursor()
                                        self.cursor.execute("DELETE FROM director WHERE  nombre =%s  ",self.tuplaa)      
                                        self.connection.commit ()
                                        self.connection.close()
                                    elif index == 5:
                                        anuncios = input("Ingrese el nombre del anuncio que  desea eliminar\n")
                                        datos = [anuncios]
                                        self.tuplaa = tuple(datos)
                                        self.connection = psycopg2.connect(dbname ="proyecto#3", user = "postgres", password ="3369")
                                        self.cursor = self.connection.cursor()
                                        self.cursor.execute("DELETE FROM anuncios WHERE  nombre =%s  ",self.tuplaa)      
                                        self.connection.commit ()
                                        self.connection.close()
                                    
                                    else:
                                        print("dato invalido")
                                    

                                elif dato2 == 2:
                                    print ("1. Usuarios")
                                    print ("2. Perfiles")
                                    print ("3. Peliculas")
                                    print ("4. Actores")
                                    print ("5. Anuncios")
                                    index = int(input("Seleccione el valor que desea:\n"))
                                    if index == 1:
                                        usuario = input ('Ingresa el nombre del usuario Administrador que deseas agregar')
                                        password = input("Ingresa tu contraseña")
                                        emal = usuario+ '@gmail.com'
                                        sus = ["Premium", "Familiar","Gratis"]
                                        susA = random.choice(sus)
                                        tU = ["Administrador", "Usuario Estandar"]
                                        tUa = random.choice(tU)
                                        h = sha256()
                                        h.update(password.encode())
                                        contraHash= h.hexdigest()
                                        datos = [usuario, contraHash,emal,susA,  tUa ]
                                        self.tuplaa = tuple(datos)
                                        self.connection = psycopg2.connect(dbname ="proyecto#3", user = "postgres", password ="3369")
                                        self.cursor = self.connection.cursor()
                                        self.cursor.executemany("insert into usuarios(usuario,password,email,tipo_suscripcion,tipo_usuarios) values(%s,	%s,	%s,	%s,	%s)",[self.tuplaa])       
                                        self.connection.commit ()
                                        self.connection.close()
                        
                                elif dato2 == 3:
                                    print ("1. Usuarios")
                                    print ("2. Perfiles")
                                    print(" 3. Peliculas")
                                    print ("4. Actores")
                                    print ("5. Anuncios")


                            elif dato == 5:
                                import reporteria

                            else:
                                print ("opcion invalida")


                            ejecucion = False
                else:
                    print(" ______________________")
                    print("|   Bienvenido         |")
                    print("|______________________|")
                    self.connection.commit ()
                    self.connection.close()
                    print("Menú de operaciones")
                    print("1.Mantenimiendo de administradores")
                    print("2. Simulaciones")
                    print("3. Busqueda")
                    print("4. Opciones avanzadas")
                    print("5. Reporteria")
                    dato = int (input("Selecciona una opción: \n"))
                    if dato == 1:
                        import Crear
                        print ("administrador creado con éxito")
                    elif dato == 2:
                        import simulacion
                    elif dato == 3:
                        import buscar
                    elif dato == 4:
                        print ("1.Eliminar")
                        print ("2.Agregar")
                        print ("3.Modificar")
                        dato2  = int(input ("Ingrese la opcion que desea:\n"))
                        if dato2 == 1:
                            print ("1. Usuarios")
                            print ("2. Perfiles")
                            print(" 3. Peliculas")
                            print ("4. Directores")
                            print ("5. Anuncios")
                            index = int(input ("Seleccione una opcion"))
                            if index == 1:
                                usuario = input("Ingrese el nombre del usuario que  desea eliminar\n")
                                datos = [usuario]
                                self.tuplaa = tuple(datos)
                                self.connection = psycopg2.connect(dbname ="proyecto#3", user = "postgres", password ="3369")
                                self.cursor = self.connection.cursor()
                                self.cursor.execute("DELETE FROM usuarios WHERE  usuario =%s  ",self.tuplaa)      
                                self.connection.commit ()
                                self.connection.close()
                            elif index == 2:
                                perfil = input("Ingrese el nombre del perfil que  desea eliminar\n")
                                datos = [perfil]
                                self.tuplaa = tuple(datos)
                                self.connection = psycopg2.connect(dbname ="proyecto#3", user = "postgres", password ="3369")
                                self.cursor = self.connection.cursor()
                                self.cursor.execute("DELETE FROM perfiles WHERE  nombre_perfil =%s  ",self.tuplaa)      
                                self.connection.commit ()
                                self.connection.close()
                            elif index == 3:
                                    pelicula = input("Ingrese el nombre de la pelicula que  desea eliminar\n")
                                    datos = [pelicula]
                                    self.tuplaa = tuple(datos)
                                    self.connection = psycopg2.connect(dbname ="proyecto#3", user = "postgres", password ="3369")
                                    self.cursor = self.connection.cursor()
                                    self.cursor.execute("DELETE FROM peliculas WHERE  titulo =%s  ",self.tuplaa)      
                                    self.connection.commit ()
                                    self.connection.close()
                            elif index == 4:
                                    director = input("Ingrese el nombre del director que  desea eliminar\n")
                                    datos = [director]
                                    self.tuplaa = tuple(datos)
                                    self.connection = psycopg2.connect(dbname ="proyecto#3", user = "postgres", password ="3369")
                                    self.cursor = self.connection.cursor()
                                    self.cursor.execute("DELETE FROM director WHERE  nombre =%s  ",self.tuplaa)      
                                    self.connection.commit ()
                                    self.connection.close()
                            elif index == 5:
                                    anuncios = input("Ingrese el nombre del anuncio que  desea eliminar\n")
                                    datos = [anuncios]
                                    self.tuplaa = tuple(datos)
                                    self.connection = psycopg2.connect(dbname ="proyecto#3", user = "postgres", password ="3369")
                                    self.cursor = self.connection.cursor()
                                    self.cursor.execute("DELETE FROM anuncios WHERE  nombre =%s  ",self.tuplaa)      
                                    self.connection.commit ()
                                    self.connection.close()
                            
                            else:
                                print("dato invalido")
                            

                        elif dato2 == 2:
                            print ("1. Usuarios")
                            print ("2. Perfiles")
                            print(" 3. Peliculas")
                            print ("4. Actores")
                            print ("5. Anuncios")
                            index = int(input("Seleccione el valor que desea:\n"))
                            if index == 1:
                                usuario = input ('Ingresa el nombre del usuario Administrador que deseas agregar')
                                password = input("Ingresa tu contraseña")
                                emal = usuario+ '@gmail.com'
                                sus = ["Premium", "Familiar","Gratis"]
                                susA = random.choice(sus)
                                tU = ["Administrador", "Usuario Estandar"]
                                tUa = random.choice(tU)
                                h = sha256()
                                h.update(password.encode())
                                contraHash= h.hexdigest()
                                datos = [usuario, contraHash,emal,susA,  tUa ]
                                self.tuplaa = tuple(datos)
                                self.connection = psycopg2.connect(dbname ="proyecto#3", user = "postgres", password ="3369")
                                self.cursor = self.connection.cursor()
                                self.cursor.executemany("insert into usuarios(usuario,password,email,tipo_suscripcion,tipo_usuarios) values(%s,	%s,	%s,	%s,	%s)",[self.tuplaa])       
                                self.connection.commit ()
                                self.connection.close()
                
                    
                        elif dato2 == 3:
                            print ("1. Usuarios")
                            print ("2. Perfiles")
                            print(" 3. Peliculas")
                            print ("4. Actores")
                            print ("5. Anuncios")


                    elif dato == 5:
                            import reporteria

                    else:
                        print ("opcion invalida")


                    ejecucion = False
            elif tipoC == "usuario estandar":
                usuario = input("ingrese su usuario  \n")
                con = input ("ingrese su contraseña  \n")
                contra = "Usuario Estandar"
                datos = [usuario,contra,con]
                self.tuplas = tuple(datos)
                self.connection = psycopg2.connect(dbname ="proyecto#3", user = "postgres", password ="3369")
                self.cursor = self.connection.cursor()
                self.cursor.execute("SELECT* FROM usuarios WHERE usuario=%s and tipo_usuarios=%s and password = %s" ,self.tuplas)        
                row =self.cursor.fetchone()
                if row == None:
                    ejecucion  = True
                    print(" __________")
                    print("|   Error\n|")
                    print("|__________|")
                    print("no eres un usuario estandar")
                    while (ejecucion == True):
                        usuario = input("ingrese su usuario  \n")
                        con = input ("ingrese su contraseña  \n")
                        contra = "Usuario Estandar"
                        datos = [tipoC,contra]
                        self.tuplas = tuple(datos)
                        datos = [usuario,contra]
                        self.tuplas = tuple(datos)
                        self.connection = psycopg2.connect(dbname ="proyecto#3", user = "postgres", password ="3369")
                        self.cursor = self.connection.cursor()
                        self.cursor.execute("SELECT* FROM usuarios WHERE usuario=%s and tipo-usuarios=%s",self.tuplas)
                        row =self.cursor.fetchone()

                        if row == None:
                            print(" __________")
                            print("|   Error  |")
                            print("|__________|")
                            print("no eres un usuario estandar")
                        else:
                            print(" ______________________")
                            print("|  Bienvenido          |")
                            print("|______________________|")
                            self.connection.commit ()
                            self.connection.close()
                            print("Menú de operaciones")
                            print("1.Mantenimiendo de administradores")
                            print("2. Simulaciones:")
                            print("3. Busqueda")
                            dato = int (input("Selecciona una opción: \n"))
                            if dato == 1:
                                import Crear
                                print ("administrador creado con éxito")
                            elif dato == 2:
                                import simulacion
                            elif dato == 3:
                                import buscar
                            else:
                                print ("opcion invalida")
                            
            
                        ejecucion = False
            else:
                print("Dato invalido")
        ejecucion= False

        
p = paginaP()
p.principal()