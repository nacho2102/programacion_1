from os import system

def imprimir_menu():# -> Imprime por consola el menu de opciones.
    menu = print("Menu a imprimir")# -> Imprime el menu de opciones.
    return menu# -> Retorna el menu de opciones.

def menu():# -> Llama a la función 'imprimir_menu', pide al usuario que ingrese una opción y la retorna.
    retorno = False# -> Inicializa la variable 'retorno' en 'False'.
    imprimir_menu()# -> Llama a la función 'imprimir_menu'.
    opcion = input("Ingresa una opcion: ")# -> Pide al usuario que ingrese una opción.
    if opcion.upper() >= "A" and opcion.upper() <= "Z":# -> Verifica que la opción ingresada sea válida entre un rango, por ejemplo entre 'A' y 'Z'.
        retorno = opcion.upper()# -> Retorna la opción ingresada.
    return retorno# -> Retorna la opción ingresada en mayúsculas, o 'False' si la opción no es válida.

def pausa():# -> Pausa la ejecución del programa.
    var = input("Presione Enter para continuar...")# -> Pausa la ejecución del programa hasta que se presione Enter.
    system ("cls")# -> Limpia la consola.

def app():# -> Programa principal.
    continuar = True# -> Inicializa la variable 'continuar' en 'True'.
    necesario = False# -> Inicializa la variable 'necesario' en 'False'.
    while continuar:# -> Ciclo 'while' que se ejecuta mientras la variable 'continuar' sea 'True'.
        opcion = menu()# -> Llama a la función 'menu' y lo asigna a la variable 'opcion'.
        system('cls')# -> Limpia la consola.
        if opcion == "A":# -> Verifica si la opción ingresada es 'A'.
            """Procesos necesarios para empezar a operar el programa.
            Ej: Cargar archivo. """
            necesario = True# -> Asigna 'True' a la variable 'necesario'.
            pausa()# -> Pausa la ejecución del programa hasta que se presione Enter.
        elif necesario == False:# -> Verifica si la variable 'necesario' es 'False'.
            print("No se llevo a cabo los procesos necesarios")# -> Imprime por consola 'No se llevo a cabo los procesos necesarios'.
            pausa()# -> Pausa la ejecución del programa hasta que se presione Enter.
        elif necesario == True:# -> Verifica si la variable 'necesario' es 'True'.
            match(opcion):# -> Verifica la opción ingresada.
                case "B":# -> Verifica si la opción ingresada es 'B'.
                    """B – Procesos correspondientes a la opción 'B'."""
                case "C":# -> Verifica si la opción ingresada es 'C'.
                    """C – Procesos correspondientes a la opción 'C'."""
                case "D":# -> Verifica si la opción ingresada es 'D'.
                    """D – Submenu opcional de procesos correspondiente a la opción 'D'."""
                    continuar_submenu = True# -> Asigna 'True' a la variable 'continuar_submenu'.
                    while continuar_submenu:# -> Ciclo 'while' que se ejecuta mientras la variable 'continuar_submenu' sea 'True'.
                        opcion_2 = menu()# -> Llama a la función 'menu' y lo asigna a la variable 'opcion_2'.
                        match(opcion_2):# -> Verifica la opción ingresada.
                            case "1":# -> Verifica si la opción ingresada es '1'.
                                """1 - Procesos correspondientes a la opción '1'."""
                            case "2":# -> Verifica si la opción ingresada es '2'.
                                """2 - Procesos correspondientes a la opción '2'."""
                            case "3":# -> Verifica si la opción ingresada es '3'.
                                """3 - Salir del submenu."""
                                continuar_submenu = False# -> Asigna 'False' a la variable 'continuar_submenu'.
                            case _ :# -> Verifica si la opción ingresada no es válida.
                                print("Opcion invalida")# -> Imprime por consola 'Opcion invalida'.
                        pausa()# -> Pausa la ejecución del programa hasta que se presione Enter.
                case "E":# -> Verifica si la opción ingresada es 'E'.
                    """E – Salir del programa."""
                    continuar = False# -> Asigna 'False' a la variable 'continuar', finalizando el programa.
                case _ :# -> Verifica si la opción ingresada no es válida.
                    print("Opcion invalida")# -> Imprime por consola 'Opcion invalida'.
            pausa()# -> Pausa la ejecución del programa hasta que se presione Enter.