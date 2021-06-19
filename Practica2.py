from os import system

menu = ["Cambiar contraseña","Ingresar coordenadas actuales", "Ubicar zona Wifi mas cercana",
            "Guardar archivo con ubicación cercana","Actualizar registro de zona wifi desde archivo",
            "Elegir opcion de menu favorita", "Cerrar sesión"]
opcion = 0
cont = 0
msj = "Error"
'''
print ("Bienvenido al sistema de ubicación para zonas públicas WIFI")
usuario = (input ("Nombre de Usuario: "))
captcha = 726 + ((5*1+7)/6)#Calcula el captcha de inicio de sesion
if usuario != "51726" : #Valida si el usuario es diferente al predefinido
    print ("ERROR, usuario incorrecto")
elif  (input ("Contraseña: ")) != "62715":  #Valida si la contraseña es diferente a la predefinida
    print ("ERROR, contraseña incorrecta")
else:
    captcha_usuario = int(input ("726 + 2: ")) #Valida si el captcha es correcto
    if captcha_usuario != captcha:
        print("ERROR, Captcha equivocado")
    else:
    '''
while opcion != "7":
            print("1. "+ menu[0]+"\n2. " + menu[1]+ "\n3. "+ menu[2]+ "\n4. "+ menu[3]+"\n5. "+ menu[4]+
                "\n6. "+ menu[5]+"\n7. "+ menu[6]+"\n")
            opcion = input("Elija una opción: ")
            
            
            if opcion == "1":
                print("Usted ha elegido la opción 1")
                opcion = "7"
            elif opcion == "2":
                print("Usted ha elegido la opción 2")
                opcion = "7"
            elif opcion == "3":
                print("Usted ha elegido la opción 3")
                opcion = "7"
            elif opcion == "4":
                print("Usted ha elegido la opción 4")
                opcion = "7"
            elif opcion == "5":
                print("Usted ha elegido la opción 5")
                opcion = "7"
            elif opcion == "6": 
                cont = 0
                fav = int(input("Seleccione opción favorita: "))
                if fav > 5 or fav < 1:
                    print("Error")
                    opcion = "7"                    
                else:   
                    valor1 = input("Ingrese el 2: ")
                    if valor1 != "2":
                        print("Error")
                    else:
                        valor2 = input("Ingrese el 6: ")                    
                        if valor2 != "6":
                            print("Error")
                        else:
                            temp = menu[int(fav)-1]
                            menu.remove(temp)
                            menu.insert(0, temp)
                            system("clear") 
                            
            elif opcion == "7":
                opcion = "7"
                print("Hasta pronto")
            else:
                print("Error")
                cont+=1
                if cont >= 3:
                    opcion = "7"      
