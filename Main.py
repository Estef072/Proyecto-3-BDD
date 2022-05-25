###  inicio 


class Main:

    def iniciar():
        ejecucion = True
        while(ejecucion == True):
            print("Bienvenido a nuetro programa de reproducción")
            print (" ________________________________________________")
            print ("|              1.Crear Cuenta                    |")
            print ("|              2.Sing in                         |")
            print ("|________________________________________________|")
            dato = int(input("Ingrese la opcion que desea realizar : \n"))
            
            
            if(dato == 1):
                print("llamar a la creacion de cuenta jaja")
            elif (dato == 2):

                call = Main.llamar()
                
            else:
                print("Opcion invalida ")
            
            ejecucion = False


    def llamar():

        import Login
           
            



Main.iniciar()