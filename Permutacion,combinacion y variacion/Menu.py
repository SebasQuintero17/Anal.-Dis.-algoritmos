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
                            "║ 1) variaciones con repeticion    ║ \n"+
                            "║ 2) Permutacion ordinaria         ║ \n"+
                            "║ 0) Salir                         ║ \n"+
                            "║                                  ║ \n"+
                            "╚══════════════════════════════════╝ \n" ))
        if opcion_menu == 1:
            sub_menu1()
        elif opcion_menu ==2:
            sub_menu2()
        elif opcion_menu == 0:
            print("Fin del Programa....")
            break 
        else:
            print("Opcion no valida")
        


def sub_menu1():


def sub_menu2():
