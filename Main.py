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
                call = Main.llamarR()
                call2 = Main.llamar()
                call3 = Main.llamarP()

            elif (dato == 2):

                call = Main.llamar()
                call2 = Main.llamarP()
                
            else:
                print("Opcion invalida ")
            
            ejecucion = False


    def llamar():

        import Login
           
    def llamarR():

        import Register 

    def llamarP ():
        import paginaP


Main.iniciar()