import psycopg2
from hashlib import sha256

class crear ():
    def administradores (self):
        usuario = input ('Ingresa el nombre del usuario Administrador que deseas agregar')
        password = input("Ingresa tu contraseña")
        emal = usuario+ '@gmail.com'
        sus = 'Premium'
        tipoUs = 'Administrador'
        h = sha256()
        h.update(password.encode())
        contraHash= h.hexdigest()
        datos = [usuario, contraHash,emal,sus, tipoUs]
        self.tuplaa = tuple(datos)
        self.connection = psycopg2.connect(dbname ="proyecto#3", user = "postgres", password ="3369")
        self.cursor = self.connection.cursor()
        self.cursor.executemany("insert into usuarios(usuario,password,email,tipo_suscripcion,tipo_usuarios) values(%s,	%s,	%s,	%s,	%s)",[self.tuplaa])       
        self.connection.commit ()
        self.connection.close()


        

c=crear()
c.administradores ()

