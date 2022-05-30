
import psycopg2 
class paginaP:
    def principal (self):
        print("A que tipo de usuario perteneces:")
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
                        print(" ______________________")
                        print("|  Bienvenido          |")
                        print("|______________________|")
                        self.connection.commit ()
                        self.connection.close()
                        print("Menú de operaciones")
                        print("1.Mantenimiendo de administradores")
                        print("2. Simulaciones")
                        dato = int (input("Selecciona una opción: \n"))
                        if dato == 1:
                            print ("nada jaja")
                        elif dato == 2:
                            print ("nada X2")
                        else:
                            print ("opcion invalida")


                        ejecucion = False
            else:
                print(" ______________________")
                print("|   Bienvenido         |")
                print("|______________________|")
                self.connection.commit ()
                self.connection.close()
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
                        print("2. Bitacora:")
                        print("3. Simulaciones")
                        dato = int (input("Selecciona una opción: \n"))
                        if dato == 1:
                            print ("nada jaja")
                        elif dato == 2:
                            print ("nada X2")
                        elif dato == 3: 
                            print("nada X3")
                        else:
                            print ("opcion invalida")
                        
                    ejecucion = False


        
p = paginaP()
p.principal()