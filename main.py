import grafo,busquedas
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
3 - Realizar una busqueda
4 - 
5.- 
6.- 
7.- Salir
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

def menuBusqueda(graph,cost):
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
			print("\033[0m---Busqueda General---\n")
			# llamamos a la funcion nodos del modulo grafo
			inicio,meta = grafo.nodos()
      		# llamamos a la funcion busqueda_general del modulo busquedas
			busquedas.busqueda_general(graph,cost,inicio,meta)
		case 2:
      		#limpia la pantalla 
			system('clear')
      		# mensaje de Búsqueda a Profundidad
			print("\033[0m---Búsqueda a Profundidad---\n")		
			# llamamos a la funcion nodos del modulo grafo
			inicio,meta = grafo.nodos()
     		# llamamos a la funcion busquedaAProfundidad del modulo busquedas
			busquedas.busquedaAProfundidad(graph,inicio, meta)
    	# tercer caso 
		case 3:
     		#limpiamos la pantalla 
			system('clear')
      		#mensaje de Búsqueda por Dijkstra 
			print("\033[0m---Búsqueda por Dijkstra---\n")		
			# llamamos a la funcion nodos del modulo grafo
			inicio, meta = grafo.nodos()
      		#llamamos a la funcion dijkstra del modulo busquedas
			busquedas.dijkstra(graph,inicio, meta,cost)
		case 4:
      		#limpiamos la pantalla 
			system('clear')
	 		#llamamos a la funcion menu
			menu()
		case _:
			print("\033[31mIngrese una opción válida")

def menu(graph,cost):
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
			grafo.graficaGrafo(graph)
    # tercer caso 
		case 3:
      #limpia la pantalla 
			system('clear')
      #mensaje de Realizar una Búsqueda
			print("\033[0m---Realizar una Búsqueda---\n")
      #se guarda en la funcion menuBusqueda
			menuBusqueda(graph,cost)
    #cuarto caso 
		case 4:
      #limpiar pantalla 
			system('clear')
      #muestra la opcion de prestamo del libro
			print("\033[0m---Prestamo de libros---\n")
      #llama  a la funcion 
    #quinto caso
		case 5:
      #limpia la pantalla
			system('clear')
      #mensaje de notificacion
			print("\033[0m---Notificaciones---\n")
      #llamamos a la funcion de notificacion
    #sexto caso 
		case 6:
      #limpia la pantalla 
			system('clear')
      #muestra la opcion del siguimiento de libros
			print("\033[0m---Seguimiento libros---\n")
      #llamamos a la funcion de seguimiento de libros
    #septimo caso
		case 7:
            #mensaje de agradecimiento al usuario
			print("\033[36mGracias... ¡Vuelve pronto!")
      #cierra el programa 
		case _:
			print("\033[31mIngrese una opción válida")



if __name__ == "__main__":
	#Llamamos a la funcion para que cree el grafo
	grafo,costos = grafo.creacionGrafo()
	menu(grafo,costos)

	#Imprimimos el nodo y el grafo en modo de lista de listas y en un diccionario para los costos
	#print(graph, cost)
	#print(rutas)
	# Imprime cada ruta y su costo encontrado.
	#for ruta, costo in rutas:
	#	print("Ruta:", ruta, "Costo:", costo)
