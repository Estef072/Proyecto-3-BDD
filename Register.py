
import psycopg2
from hashlib import sha256



class Register:
    def registrarse (self):
        correo = input("Ingrese su correo electronico \n")
        usuario = input("Ingrese su nombre usuario\n ")
        contra = input("Ingrese  su Contraseña \n ")
        confiContra = input("confirme su Contraseña \n")
        suscris =input("ingrese su tipo de susripcion \n")
        tipoUs = input("ingrese su tipo de usuario\n")
        h = sha256()
        h.update(contra.encode())
        contraHash= h.hexdigest()
        

        datos = [usuario, contraHash,correo,suscris, tipoUs]
        self.tuplaa = tuple(datos)
        self.connection = psycopg2.connect(dbname ="proyecto#3", user = "postgres", password ="3369")
        self.cursor = self.connection.cursor()
        self.cursor.executemany("insert into usuarios(usuario,password,email,tipo_suscripcion,tipo_usuarios) values(%s,	%s,	%s,	%s,	%s)",[self.tuplaa])       
        self.connection.commit ()
        self.connection.close()


        if (confiContra != contra ):
            print(" _________________________________")
            print("| Las contraseñas no son iguales  |")
            print("|_________________________________|")
            ejecucion  = True
            while (ejecucion == True):
                correo = input("Ingrese su correo electronico \n")
                usuario = input("Ingrese su nombre usuario\n ")
                contra = input("Confirme  su Contraseña \n ")
                confiContra = input("Ingrese su usuario \n")
                print("Tipos de suscripciones")
                print("1.Premium")
                print("1.Familiar")
                print("1.Gratis")
                suscris = input("Selecciona tu suscripcion:\n")
                print ("Tipos de usuarios")
                print("Usuario regular ")
                print("Usuario regular ")
                tipoUs = input("Selecciona el tipo de usuario que deseas \n")

                datos = [usuario, self.contraHash,correo,suscris, tipoUs]
                self.tuplaa = tuple(datos)
                self.connection = psycopg2.connect(dbname ="Proyecto#3", user = "postgres", password ="3369")
                self.cursor = self.connection.cursor()
                self.cursor.executemany("insert into usuarios(usuario,contra,email,tipo_suscripcion,activo_desde) values(%s,	%s,	%s,	%s,	%s)",self.tuplaa)       
                self.connection.commit ()
                self.connection.close()
            ejecucion = False
    

        else:
            print("  ___________________________")
            print ("|    se creo cuenta         | ")
            print(" |___________________________|")






r = Register()
r.registrarse()