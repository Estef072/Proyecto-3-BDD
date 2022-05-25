
from mimetypes import init
import psycopg2

from tkinter import messagebox

from hashlib import sha256


class Login:
    
    def loguear(self):    
            usuario = input ("Ingresa tu usuario:\n")
            contraseña = input("Ingresa tu contraseña:\n")
            datos = [usuario,contraseña]
            self.tuplas = tuple(datos)
            self.connection = psycopg2.connect(dbname ="proyecto#2", user = "postgres", password ="3369")
            self.cursor = self.connection.cursor()
            self.cursor.execute("SELECT* FROM usuarios WHERE usuario=%s and password =%s",self.tuplas)
                    
            row =self.cursor.fetchone()

            if  row == None:
                ejecucion  = True
                print(" __________")
                print("|   Error\n|")
                print("|__________|")
                while (ejecucion == True):
                    usuario = input ("Ingresa tu usuario:\n")
                    contraseña = input("Ingresa tu contraseña:\n")
                    datos = [usuario,contraseña]
                    self.tuplas = tuple(datos)
                    self.connection = psycopg2.connect(dbname ="proyecto#2", user = "postgres", password ="3369")
                    self.cursor = self.connection.cursor()
                    self.cursor.execute("SELECT* FROM usuarios WHERE usuario=%s and password =%s",self.tuplas)
                    row =self.cursor.fetchone()
                    if row == None:
                        print(" __________")
                        print("|   Error  |")
                        print("|__________|")
                    else:
                        print(" ______________________")
                        print("|   Se inicio sesion   |")
                        print("|______________________|")
                        self.connection.commit ()
                        self.connection.close()
                    ejecucion = False


            else:
                print(" ______________________")
                print("|   Se inicio sesion   |")
                print("|______________________|")
                self.connection.commit ()
                self.connection.close()

        


l= Login()
l.loguear()
