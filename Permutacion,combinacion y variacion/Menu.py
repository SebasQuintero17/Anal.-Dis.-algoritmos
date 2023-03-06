import sys

print("""
██████╗░██╗███████╗███╗░░██╗██╗░░░██╗███████╗███╗░░██╗██╗██████╗░░█████╗░
██╔══██╗██║██╔════╝████╗░██║██║░░░██║██╔════╝████╗░██║██║██╔══██╗██╔══██╗
██████╦╝██║█████╗░░██╔██╗██║╚██╗░██╔╝█████╗░░██╔██╗██║██║██║░░██║██║░░██║
██╔══██╗██║██╔══╝░░██║╚████║░╚████╔╝░██╔══╝░░██║╚████║██║██║░░██║██║░░██║
██████╦╝██║███████╗██║░╚███║░░╚██╔╝░░███████╗██║░╚███║██║██████╔╝╚█████╔╝
╚═════╝░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═╝╚═════╝░░╚════╝░""")




def menu():
        
    while True:
        opcion_menu= int(input("╔═══════════════════════════════╗ \n"+
                            "║ 𝔐𝔢𝔫𝔲́                             ║ \n"+ 
                            "║                                  ║ \n"+
                            "║       Elije una opción           ║ \n"+
                            "║ 1) El orden Importa              ║ \n"+
                            "║ 2) El orden no importa           ║ \n"+
                            "║ 0) Salir                         ║ \n"+
                            "║                                  ║ \n"+
                            "╚══════════════════════════════════╝ \n" ))
        if opcion_menu == 1:
            sub_menu1()
        elif opcion_menu ==2:
            sub_menu2()
        elif opcion_menu == 0:
            print("Fin del Programa....")
            sys.exit()
        else:
            print("Opcion no valida")
        


def sub_menu1():
    while True:
        opcion_sub_menu1 =  int(input("╔═══════════════════════════════════════╗ \n"+
                            "║ 𝔐𝔢𝔫𝔲́                                     ║ \n"+ 
                            "║                                          ║ \n"+
                            "║         Elije una opción                 ║ \n"+
                            "║ 1) Todos los elementos intervienen       ║ \n"+
                            "║ 2) No todos los elementos intervienen    ║ \n"+
                            "║ 3) Regresar al menú aterior              ║ \n"+
                            "║ 0) Salir                                 ║ \n"+
                            "║                                          ║ \n"+
                            "╚══════════════════════════════════════════╝ \n" ))
        
        if opcion_sub_menu1 == 1:
            while True:
                opcion_sub_menu1_1 =  int(input("╔═══════════════════════════════════════╗ \n"+
                                    "║ 𝔐𝔢𝔫𝔲́                                     ║ \n"+ 
                                    "║                                          ║ \n"+
                                    "║         Elije una opción                 ║ \n"+
                                    "║ 1) Los elementos se repiten              ║ \n"+
                                    "║ 2) Los elementos no se repite            ║ \n"+
                                    "║ 3) Regresar al menú aterior              ║ \n"+
                                    "║ 0) Salir                                 ║ \n"+
                                    "║                                          ║ \n"+
                                    "╚══════════════════════════════════════════╝ \n" ))
                
                if opcion_sub_menu1_1 == 1:
                    print("Uste esta haciendo una Permutacion con Repeticion ")
                    return menu()
                elif opcion_sub_menu1_1 == 2:
                    print("Usted esta haciendo una Permutacion Ordinaria")
                    return menu()
                elif opcion_sub_menu1_1 == 3:
                    print("Regresando al menú anterior....")
                    return
                elif opcion_sub_menu1_1 == 0:
                    print("Fin del Programa....")
                    sys.exit()
                else:
                    print("Opcion no valida")

        elif opcion_sub_menu1 ==2:
            while True:
                opcion_sub_menu1_1 =  int(input("╔═══════════════════════════════════════╗ \n"+
                                    "║ 𝔐𝔢𝔫𝔲́                                     ║ \n"+ 
                                    "║                                          ║ \n"+
                                    "║         Elije una opción                 ║ \n"+
                                    "║ 1) Los elementos se repiten              ║ \n"+
                                    "║ 2) Los elementos no se repite            ║ \n"+
                                    "║ 3) Regresar al menú aterior              ║ \n"+
                                    "║ 0) Salir                                 ║ \n"+
                                    "║                                          ║ \n"+
                                    "╚══════════════════════════════════════════╝ \n" ))
                
                if opcion_sub_menu1_1 == 1:
                    print("Uste esta haciendo una Permutacion con Repeticion ")
                    return menu()
                elif opcion_sub_menu1_1 == 2:
                    print("Usted esta haciendo una Permutacion Ordinaria")
                    return menu()
                elif opcion_sub_menu1_1 == 3:
                    print("Regresando al menú anterior....")
                    return
                elif opcion_sub_menu1_1 == 0:
                    print("Fin del Programa....")
                    sys.exit()
                else:
                    print("Opcion no valida")
            
        

        elif opcion_sub_menu1 == 3:
            print("Regresando al menú anterior....")
            return
        elif opcion_sub_menu1 == 0:
            print("Fin del Programa....")
            sys.exit()
        else:
            print("Opcion no valida")




def sub_menu2():
    while True:
        opcion_sub_menu2 =  int(input("╔══════════════════════════════════════════╗ \n"+
                            "║ 𝔐𝔢𝔫𝔲́                                     ║ \n"+ 
                            "║                                          ║ \n"+
                            "║         Elije una opción                 ║ \n"+
                            "║ 1) Los elementos se repiten              ║ \n"+
                            "║ 2) Los elementos no se repite            ║ \n"+
                            "║ 3) Regresar al menú aterior              ║ \n"+
                            "║ 0) Salir                                 ║ \n"+
                            "║                                          ║ \n"+
                            "╚══════════════════════════════════════════╝ \n" ))
        
        if opcion_sub_menu2 == 1:
            print("Uste esta haciendo una Combinacion con Repeticion ")
            return menu()
        elif opcion_sub_menu2 == 2:
            print("Usted esta haciendo una Combinacion Ordinaria")
            return menu()
        elif opcion_sub_menu2 == 3:
            print("Regresando al menú anterior....")
            return
        elif opcion_sub_menu2 == 0:
            print("Fin del Programa....")
            sys.exit()
        else:
            print("Opcion no valida")
    

menu()