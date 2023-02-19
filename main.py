import grafo as grafos
import busquedas
from os import system

def regresarmenu():
	"""
  Funcion: Esta función permite regresar al menu principal si es que se encuentra dentro de una opcion

 Parametros: No tiene parámetros

 Retorna: No retorna ningún valor
 	"""
	system("clear")
	menu()

#variable menuPrincipal que contiene todo el menú de opciones escrito
menuPrincipal = """PoolCleaning
----------------------------------
1 - Inicializar agente
2 - Mostrar grafo
3 - Realizar busqueda de la piscina más sucia
4 - Ver conexiones y costos de cada nodo
5.- Limpiar todas las piscinas empezando desde la más sucia
6.- Salir
------
"""

#variable menuPrincipal que contiene todo el menú de opciones escrito
menuBusquedas = """PoolCleaning
----------------------------------
1 - Búsqueda General
2 - Búsqueda a Profundidad
3 - Búsqueda Dijkstra
4.- Regresar al menu principal
------
"""

def menu():
	"""
  Funcion: L afuncion menu, nos mostrara en pantalla todos los procesos que tiene el software 

 Parametros: No, contiene ningun parametro

 Retorna: No, retorna ningun dato 
 	"""
	print(f"\033[36m{menuPrincipal}")
  #el bucle while para que el usuario ingrese la opcion correcta
	while True:
	    try:
        #mensaje de ingreso de opcion
	        opcion = int(input("\033[0mIngrese una opción: "))
	        break
        # si la opcion ingresada por el usuario es incorrecta nos mostara un error 
	    except ValueError:
        #mensaje que pide al usuario que ingrese de nuevo la opcion correcta
	        print("\033[31mEntrada inválida, ingrese solo numeros")
        #limpia la pantalla
	        system("clear")
        # muestra el menu de opciones 
	        menu()
        
	match opcion:
  #primer caso 
		case 1:
      #limpia la pantalla 
			system('clear')
      # mensaje de inicializar agente
			print("\033[0m---Inicializar agente---\n")
      # se guarda en la funcion de registro de estudiante 
    #segundo caso 
		case 2:
      #limpia la pantalla 
			system('clear')
      # mensaje de mostrar grafo
			print("\033[0m---Mostrar Grafo---\n")
      # se guarda en la funcion de catalogo 
			grafos.graficaGrafo(grafo)
    # tercer caso 
		case 3:
      #limpia la pantalla 
			system('clear')
      #mensaje de Realizar una Búsqueda
			print("\033[0m---Realizar una Búsqueda---\n")
      #llamamos la funcion menuBusqueda
			menuBusqueda()
    #cuarto caso 
		case 4:
      #limpiar pantalla 
			system('clear')
      #imprime mensaje Ver conexiones y costos de cada nodo
			print("\033[0m---Ver conexiones y costos de cada nodos---\n")
      #llama  a la funcion mostrarConexionesNodos del modulo grafo
			grafos.mostrarConexionesNodos(grafo,costos)
    #quinto caso
		case 5:
      #limpia la pantalla
			system('clear')
      #mensaje de Limpiar todas las piscinas empezando desde la más sucia
			print("\033[0m---Limpiar todas las piscinas empezando desde la más sucia---\n")
		#llamamos a la funcion mostrarEstadosPiscinas del modulo grafo para mostrar todas las piscinas y sus estados antes de la limpieza
			grafos.mostrarEstadosPiscinas(estados)
      #llamamos a la funcion limpiarDesdePiscinaMasSucia del modulo grafo
			grafos.limpiarDesdePiscinaMasSucia(estados)
		#llamamos a la funcion mostrarEstadosPiscinas del modulo grafo para mostrar todas las piscinas y sus estados después de la limpieza
			grafos.mostrarEstadosPiscinas(estados)
		#sexto caso
		case 6:
            #mensaje de agradecimiento al usuario
			print("\033[36mGracias... ¡Vuelve pronto!")
      		#cierra el programa 
			exit()
		#caso que no ingrese ningun caracter
		case _:
			#imprimimos que la opcion no es valida
			print("\033[31mIngrese una opción válida")


def menuBusqueda():
	"""
  Funcion: Nos mostrará en pantalla todo el menú referente a los algoritmos de busqueda disponibles

 Parametros: No, contiene ningun parametro

 Retorna: No, retorna ningun dato 
 	"""
	print(f"\033[36m{menuBusquedas}")
  #el bucle while para que el usuario ingrese la opcion correcta
	while True:
	    try:
        #mensaje de ingreso de opcion
	        opcion = int(input("\033[0mIngrese una opción: "))
	        break
        # si la opcion ingresada por el usuario es incorrecta nos mostara un error 
	    except ValueError:
        #mensaje que pide al usuario que ingrese de nuevo la opcion correcta
	        print("\033[31mEntrada inválida, ingrese solo numeros")
        #limpia la pantalla
	        system("clear")
        # muestra el menu de opciones 
	        menu()
        
	match opcion:
  #primer caso 
		case 1:
     		#limpia la pantalla 
			system('clear')
      		# mensaje de inicializar agente
			print("\033[0m---Busqueda General---\n")
			#se comprueba si todos los elementos de la lista "estados" son iguales al primer elemento
			if all(x == estados[0] for x in estados):
				#imprimimos que todas las piscinas están limpias
			    print("Todas las piscinas se encuentran limpias.")
			#caso contrario
			else:
				#llamamos a la funcion mostrarEstadosPiscinas del modulo grafo para mostrar todas las piscinas y sus estados antes de la limpieza
				grafos.mostrarEstadosPiscinas(estados)
				# llamamos a la funcion nodos del modulo grafo
				inicio,meta = grafos.nodos()
	      		# llamamos a la funcion busqueda_general del modulo busquedas
				busquedas.busqueda_general(grafo,costos,inicio,meta)
		case 2:
      		#limpia la pantalla 
			system('clear')
      		# mensaje de Búsqueda a Profundidad
			print("\033[0m---Búsqueda a Profundidad---\n")	
			#se comprueba si todos los elementos de la lista "estados" son iguales al primer elemento
			if all(x == estados[0] for x in estados):
				#imprimimos que todas las piscinas están limpias
			    print("Todas las piscinas se encuentran limpias.")
			#caso contrario
			else:
				#llamamos a la funcion mostrarEstadosPiscinas del modulo grafo para mostrar todas las piscinas y sus estados antes de la limpieza
				grafos.mostrarEstadosPiscinas(estados)
				# llamamos a la funcion nodos del modulo grafo
				inicio,meta = grafos.nodos()
	     		# llamamos a la funcion busquedaAProfundidad del modulo busquedas
				busquedas.busquedaAProfundidad(grafo,inicio, meta,estados,costos)
    	# tercer caso 
		case 3:
     		#limpiamos la pantalla 
			system('clear')
      		#mensaje de Búsqueda por Dijkstra 
			print("\033[0m---Búsqueda por Dijkstra---\n")
			#se comprueba si todos los elementos de la lista "estados" son iguales al primer elemento
			if all(x == estados[0] for x in estados):
				#imprimimos que todas las piscinas están limpias
			    print("Todas las piscinas se encuentran limpias.")
			#caso contrario
			else:
				#llamamos a la funcion mostrarEstadosPiscinas del modulo grafo para mostrar todas las piscinas y sus estados antes de la limpieza
				grafos.mostrarEstadosPiscinas(estados)
				# llamamos a la funcion nodos del modulo grafo
				inicio, meta = grafos.nodos()
	      		#llamamos a la funcion dijkstra del modulo busquedas
				busquedas.dijkstra(grafo,inicio, meta,costos)
		case 4:
      		#limpiamos la pantalla 
			system('clear')
	 		#llamamos a la funcion menu
			menu()
		#caso que no ingrese ningun caracter
		case _:
			#imprimimos que la opcion no es valida
			print("\033[31mIngrese una opción válida")

if __name__ == "__main__":
	#creamos variables globales para grafo, costos y estados
	global grafo, costos, estados
	#Llamamos a la funcion para que cree el grafo
	grafo,costos,estados = grafos.creacionGrafo()
	while True:
		#Limpiamos la pantalla
		system('clear')
		#llamada a la función menu
		menu()
		#solicitamos al usuario que persione cualquier tecla
		#para continuar con el programa
		input("\n\033[0mPresione una tecla para continuar... ")
