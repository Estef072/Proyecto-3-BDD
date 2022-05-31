

import namegenerator

import string
import random

from datetime import datetime #Librería para obtener la hora.
import psycopg2   

import cryptocode

#Generar nombres aleatorios.
generador = int(input("Ingrese la cantidad de nombres que desea generar: "))

correos = ['c.analuz@yahoo.es', 'claudiocastanonmigeot@gmail.com', 'tango_negro@hotmail.com', 'pato_one@hotmail.com', '	javier_celedon@hotmail.com', 'fran.afull@live.cl', 'joacocordero@gmail.com', 'pepacordero@gmail.com'
               ,'laah.valehh@hotmail.com', 'annabeck_@hotmail.com', 'japacortes@yahoo.com', 'juanocortes@hotmail.com', 'pili_diami_angol@hotmail.com', 'tallerlaquilla@gmail.com', 'anamariadelacarrera@gmail.com', 'paulinadelacarrera@gmail.com'
               , 'fgregoriog@vtr.net', 'anto_demarchi@hotmail.com', '	Karito_1404@hotmail.com', 'loredicat@hotmail.com', 'diazma@tiscali.it', 'pablodubof@gmail.com', 'dddura69@gmail.com', 'khiton_@hotmail.com'
               , 'pecmor63@gmail.com', 'jlescote@gasco.cl', 'aespinz@hotmail.com', 'fespinosacl@yahoo.com', 'ricardo.espinosa.z@hotmail.com', 'sabelina50@yahoo.com.es', 'alvaro.espoz@gmail.com', 'patorfebre@hotmail.com', 'cfernandez@isa.cl', 
               'francis_nexos@hotmail.com', 'marcelafigueroazamora@hotmail.com', 'marcelafigueroazamora@hotmail.com', '	mafigza@gmail.com', 'marissaleone@hotmail.com', 'natygris@hotmail.com', 'consuelo.fornes@gmail.com', 
               'jmfornes@yahoo.com', 'fornickinson@hotmail.com', 'lml@vtr.net', 'xfreitte@gmail.com', 'fernandofreitte.xia@gmail.com', 'hfreitte2618@gmail.com', 'jfreitte@vtr.net', 'cfalvear@hotmail.com', 
               'debora1611@hotmail.com', 'fernando.gaete@gmail.com', 'fgaete@colegioaltamira.cl', 'panchop71@hotmail.com']
            

#Lista de nombres.
nombress = []

#Lista de apellidos.
apellidoss = []

#Lista de usuarios
usuarioss = []

## picking random characters from the list
password = ['32131', '32132', '32133', '32134', '32135','32136','32137','32138', '32139', '32140', '32141',	'32142','32143','32144', '32145','32146', '32147', '32148', '32149', '32150','32151', '32152', '32131', 
            '32132'	'32133', '32134', '32135', '32136', '32137', '32138', '32139', '32140', '32141', '32142', '32143', '32144', '32145', '32146', '32147', '32148', '32149', '32150', '32151', '32152', '32131', 
            '32132','32133', '46591', '32135','46593', '46595', '46589']

perfiless = []

planess = []

def nombres():

    #Conexión a la base de datos.
    conexion1 = psycopg2.connect(dbname ="proyecto#3", user = "postgres", password ="3369")

    cursor1 = conexion1.cursor() #Cursor de la conexión.



    sql = "INSERT INTO usuarios(usuario, password, email, tipo_suscripcion, tipo_usuarios) VALUES (%s, %s, %s, %s, %s)"

    sql2 = "INSERT INTO perfiles( nombre_perfil,usuario) VALUES (%s, %s)"

    print("Nombres \n")
    for i in range(generador):
        
        usuario = namegenerator.gen()

        print(usuario)

        
        contrasen = contrasenas()

        perf = perfiles()

        plan = seleccionPlanes(planes)
        
        tipoUs = tipous(tipos)

        cursor1.execute(sql,(usuario, contrasen, correos[i], plan,tipoUs))
        cursor1.execute(sql2, (perf,usuario))
    
    conexion1.commit()

    conexion1.close()

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def contrasenas(): 

    for i in range(generador):
        
        ff = random.choice(password)

        #Encriptando contraseña
        passkey = 'UVG' #Llave para encriptar.

        conn = cryptocode.encrypt(ff, passkey) #Contraseña encriptada.
        

    return conn

def perfiles():

    print("Perfiles \n")
    for i in range(generador):
        
        perfiles = namegenerator.gen()

        print(perfiles)

    return perfiles

planes = ["Premium", "Familiar", "Gratis"]


def seleccionPlanes(planes):
    print("Horas \n")
    for i in range(generador):

        ele = random.choice(planes)
        print(ele)

        return ele
def correo():

    for i in range(generador):
        print(correos[i])

    return correo[i]

tipos = ["Usuario Estandar", "Administrador"]

def tipous(tipos):
    print("Horas \n")
    for i in range(generador):

        ele = random.choice(tipos)
        print(ele)

        return ele
nombres()
contrasenas()
perfiles()
tipous(tipos)
seleccionPlanes(planes)
