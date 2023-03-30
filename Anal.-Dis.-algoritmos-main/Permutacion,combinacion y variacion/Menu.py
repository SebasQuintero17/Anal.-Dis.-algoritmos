import sys
import Funciones_matematicas 

print("""
██████╗░██╗███████╗███╗░░██╗██╗░░░██╗███████╗███╗░░██╗██╗██████╗░░█████╗░
██╔══██╗██║██╔════╝████╗░██║██║░░░██║██╔════╝████╗░██║██║██╔══██╗██╔══██╗
██████╦╝██║█████╗░░██╔██╗██║╚██╗░██╔╝█████╗░░██╔██╗██║██║██║░░██║██║░░██║
██╔══██╗██║██╔══╝░░██║╚████║░╚████╔╝░██╔══╝░░██║╚████║██║██║░░██║██║░░██║
██████╦╝██║███████╗██║░╚███║░░╚██╔╝░░███████╗██║░╚███║██║██████╔╝╚█████╔╝
╚═════╝░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═╝╚═════╝░░╚════╝░""")




def menu():
        
    while True:
        opcion_menu= int(input("╔══════════════════════════════════╗ \n"+
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
        opcion_sub_menu1 =  int(input("╔══════════════════════════════════════════╗ \n"+
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
                opcion_sub_menu1_1 =  int(input("╔═════════════════════════════════════════════╗ \n"+
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
                    print("Usted esta haciendo una Permutacion con Repeticion ")

                    numero_de_elementos = int(input("Ingrese número de elementos a permutar: "))
                    while numero_de_elementos <= 0:
                        print("Error: El número de elementos a permutar debe ser mayor que cero")
                        numero_de_elementos = int(input("Ingrese número de elementos a permutar: "))
                        
                        
                    lista_elementos = []
                    elemntos_agrupar = int(input("numero de elementos a agrupar: "))
                    while elemntos_agrupar <= 0:
                        print("Error: El número de elementos a agrupar debe ser mayor que cero")
                        elemntos_agrupar = int(input("numero de elementos a agrupar: "))

                    for x in range(elemntos_agrupar):
                        elemnto = int(input("Ingrese elemento a añadir: "))
                        while elemnto <= 0:
                         print("Error: El número de elementos a agrupar debe ser mayor que cero")
                         elemnto = int(input("Ingrese elemento a añadir: "))
                        lista_elementos.append(elemnto)
                        


                    Funciones_matematicas.Permutacion_con_Repeticion(numero_de_elementos,lista_elementos)
                    permutations = Funciones_matematicas.Permutacion_con_Repeticion(numero_de_elementos,lista_elementos)
                    for p in permutations:
                        print(p)
                    print("El numero de combinaciones posibles en este caso son", len(permutations))
                    return menu()
                
                elif opcion_sub_menu1_1 == 2:
                    print("Usted esta haciendo una Permutacion Ordinaria")

                    lista_elementos = []
                    elemntos_agrupar = int(input("numero de elementos a agrupar: "))
                    while elemntos_agrupar <= 0:
                         print("Error: El número de elementos a agrupar debe ser mayor que cero")
                         elemntos_agrupar = int(input("numero de elementos a agrupar: "))

                    for x in range(elemntos_agrupar ):
                        elemnto = int(input("Ingrese elemento a añadir: "))
                        while elemnto <= 0:
                         print("Error: El número de elementos a agrupar debe ser mayor que cero")
                        elemnto = int(input("Ingrese elemento a añadir: "))

                        lista_elementos.append(elemnto)
                    Funciones_matematicas.Permutacion(lista_elementos)
                    permutaciones = Funciones_matematicas.Permutacion(lista_elementos)
                    for p in permutaciones:
                        print(p)
                    print("El número de posibles permutaciones para este grupo seria: ",len(permutaciones))
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
                opcion_sub_menu1_1 =  int(input("╔══════════════════════════════════════════╗ \n"+
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
                    print("Uste esta haciendo una Variacion con Repeticion ")
                    numero_de_elementos= int(input("Ingrese número de elementos: "))
                    while numero_de_elementos <= 0:
                         print("Error: El número de elementos a agrupar debe ser mayor que cero")
                         numero_de_elementos= int(input("Ingrese número de elementos: "))
                    
                    numero_elemntos_agrupar = int(input("Ingrese número de elemntos a agrupar:  "))
                    while numero_elemntos_agrupar <= 0:
                         print("Error: El número de elementos a agrupar debe ser mayor que cero")
                         numero_elemntos_agrupar = int(input("Ingrese número de elemntos a agrupar:  "))

                    Funciones_matematicas.variation_with_repetition(numero_de_elementos,numero_elemntos_agrupar)
                    return menu()
                
                elif opcion_sub_menu1_1 == 2:
                    print("Usted esta haciendo una Variacion Ordinaria")
                    numero_de_elementos= int(input("Ingrese número de elementos: "))
                    while numero_de_elementos <= 0:
                         print("Error: El número de elementos a agrupar debe ser mayor que cero")
                         numero_de_elementos= int(input("Ingrese número de elementos: "))


                    numero_elemntos_agrupar = int(input("Ingrese número de elemntos a agrupar:  "))
                    while numero_elemntos_agrupar <= 0:
                         print("Error: El número de elementos a agrupar debe ser mayor que cero")
                         numero_elemntos_agrupar = int(input("Ingrese número de elemntos a agrupar:  "))

                    Funciones_matematicas.variacion_ordenada(numero_de_elementos,numero_elemntos_agrupar)
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
        opcion_sub_menu2 =  int(input("╔═════════════════════════════════════════════╗ \n"+
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
            numero_de_elementos= int(input("Ingrese número de elementos: "))
            while numero_de_elementos <= 0:
                         print("Error: El número de elementos a agrupar debe ser mayor que cero")
                         numero_de_elementos= int(input("Ingrese número de elementos: "))

            numero_elemntos_agrupar = int(input("Ingrese número de elemntos a agrupar:  "))
            while numero_elemntos_agrupar <= 0:
                         print("Error: El número de elementos a agrupar debe ser mayor que cero")
                         numero_elemntos_agrupar = int(input("Ingrese número de elemntos a agrupar:  "))
            
            Funciones_matematicas.combinatoria_con_repeticion(numero_de_elementos,numero_elemntos_agrupar)
            return menu()
        
        elif opcion_sub_menu2 == 2:
            print("Usted esta haciendo una Combinacion Ordinaria")
            numero_de_elementos= int(input("Ingrese número de elementos: "))
            while numero_de_elementos <= 0:
                         print("Error: El número de elementos a agrupar debe ser mayor que cero")
                         numero_de_elementos= int(input("Ingrese número de elementos: "))

            numero_elemntos_agrupar = int(input("Ingrese número de elemntos a agrupar:  "))
            while numero_elemntos_agrupar <= 0:
                         print("Error: El número de elementos a agrupar debe ser mayor que cero")
                         numero_elemntos_agrupar = int(input("Ingrese número de elemntos a agrupar:  "))
            Funciones_matematicas.combinatoria_ordinaria(numero_de_elementos,numero_elemntos_agrupar)
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
#finalizamos