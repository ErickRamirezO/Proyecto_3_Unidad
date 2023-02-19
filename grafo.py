import networkx as nx
import random
#libreria para graficar el grafo
import matplotlib.pyplot as plt
#libreria para hacer uso de colores en consola
from termcolor import colored


def creacionGrafo():
	"""
 	Función que nos permite crear una lista de lista que representa a los nodos del grafo y sus conexiones
  	además de añadir el costo a cada conexion entre nodos usando un diccionario.
   	Parámetros
	_____________
 	No tiene parámetros
  	Retorno
   	____________
	graph: grafo con todos los nodos conectados entre sí
 	cost: diccionario que contiene el costo de cada conexion entre los nodos del grafo
  	"""
	# creación del grafo y diccionario de costos
	graph, cost = [[] for i in range(21)], {}
	# añadir los nodos
	#Piscina al aire libre -> 0
	#Agua relajante -> 1
	#Agua Terapéutica -> 2
	#Piscina semicubierta -> 3
	#Piscina cubierta -> 4
	#Aguas Termales -> 5
	#Hidromasaje -> 6
	#Agua de los pequeños -> 7
	#Piscina Polar -> 8
	#Sauna -> 9
	#Turco -> 10
	#Ludicotermal -> 11
	#Caliente -> 12
	#Tibia -> 13
	#Fria -> 14
	#Salada -> 15
	#Piscina de olas -> 16
	#Aguas Mixtas -> 17
	#Familiar -> 18
	#Parque acuático -> 19
	#Chapoteo -> 20
	#0 a 7
	graph[0].append(7)
	graph[7].append(0)
	#0 a 8
	graph[0].append(8)
	graph[8].append(0)
	#7 a 1
	graph[7].append(1)
	graph[1].append(7)
	#7 a 6
	graph[7].append(6)
	graph[6].append(7)
	#7 a 8
	graph[7].append(8)
	graph[8].append(7)
	#7 a 16
	graph[7].append(16)
	graph[16].append(7)
	#1 a 2
	graph[1].append(2)
	graph[2].append(1)
	#1 a 5
	graph[1].append(5)
	graph[5].append(1)
	#2 a 3
	graph[2].append(3)
	graph[3].append(2)
	#3 a 4
	graph[3].append(4)
	graph[4].append(3)
	#4 a 5
	graph[4].append(5)
	graph[5].append(4)
	#5 a 6
	graph[5].append(6)
	graph[6].append(5)
	#6 a 9
	graph[6].append(9)
	graph[9].append(6)
	#6 a 10
	graph[6].append(10)
	graph[10].append(6)
	#9 a 11
	graph[9].append(11)
	graph[11].append(9)
	#9 a 8
	graph[9].append(8)
	graph[8].append(9)  #
	#8 a 12,13,14,15
	graph[8].append(12)
	graph[8].append(13)
	graph[8].append(14)
	graph[8].append(15)
	graph[12].append(8)
	graph[13].append(8)
	graph[14].append(8)
	graph[15].append(8)
	#16 a 17,18,19,20
	graph[16].append(17)
	graph[16].append(18)
	graph[16].append(19)
	graph[16].append(20)
	graph[17].append(16)
	graph[18].append(16)
	graph[19].append(16)
	graph[20].append(16)

	# añadiendo el costo a los nodos, todos con el valor de 1
	cost[(0, 7)] = cost[(7, 0)] = cost[(0, 8)] = cost[(8, 0)] = cost[(
	 7, 1)] = cost[(1, 7)] = cost[(7, 6)] = cost[(6, 7)] = cost[(7, 8)] = cost[(
	  8, 7)] = cost[(7, 16)] = cost[(16, 7)] = cost[(1, 2)] = cost[(
	   2, 1)] = cost[(1, 5)] = cost[(5, 1)] = cost[(2, 3)] = cost[(3, 2)] = cost[(
	    3, 4)] = cost[(4, 3)] = cost[(4, 5)] = cost[(5, 4)] = cost[(
	     5, 6)] = cost[(6, 5)] = cost[(6, 9)] = cost[(9, 6)] = cost[(
	      6, 10)] = cost[(10, 6)] = cost[(9, 11)] = cost[(11, 9)] = cost[(
	       9, 8)] = cost[(8, 9)] = cost[(8, 12)] = cost[(8, 13)] = cost[(
	        8, 14)] = cost[(8, 15)] = cost[(12, 8)] = cost[(13, 8)] = cost[(
	         14, 8)] = cost[(15, 8)] = cost[(16, 17)] = cost[(16, 18)] = cost[(
	          16, 19)] = cost[(16, 20)] = cost[(17, 16)] = cost[(18, 16)] = cost[(
	           19, 16)] = cost[(20, 16)] = 2
	# creación de la lista de estados
	states = [random.randint(1, 5) for i in range(21)]
	#retornamos el graph,cost y states
	return graph, cost, states


def graficaGrafo(grafo):
	"""
 	Función que nos permite realizar la gráfica del grafo en una interfaz gráfica
  	Parámetros
	_____________
 	grafo: lista de lista que contiene a los nodos de dicho grafo.
  	Retorno
   	____________
	No retorna ningún valor
  	"""
	#Creamos un grafo vacío, sin nodos, ni arcos
	G = nx.Graph()

	#Añadir nodos al grafo
	for i in range(21):
		G.add_node(i)

	#Añadir aristas al grafo
	for i in range(21):
		for j in grafo[i]:
			G.add_edge(i, j)

	#Dibujamos el grafo
	nx.draw(G, with_labels=True)
	#mostramos el grafo
	plt.show()


def mostrarConexionesNodos(grafo, costo):
	"""
	Función que realiza el recorrido de cada nodo del grafo para mostrar sus conexiones y costo
 	Parámetros
  	__________
  	grafo: lista de lista que contiene a los nodos de dicho grafo.
   	costo: diccionario que contiene el costo de cada conexion entre los nodos del grafo
  	Retorno
   	____________
	No retorna ningún valor
 	"""
	for i, nodo in enumerate(grafo):
		print("Nodo: ", i)
		print("Conexiones: ", nodo)
		suma_costo = 0
		for conexion in nodo:
			suma_costo += costo[(i, conexion)]
		print("Costo total: ", suma_costo)


def nodos():
	"""
 	Función que nos permite establecer cual va a ser el nodo de partido y el objetivo
   	Parámetros
	_____________
 	No tiene parámetros
  	Retorno
   	____________
	inicio: nodo desde el cual se va a partir la búsqueda
 	meta: nodo al cual se desea llegar
  	"""
	# solicitamos nodo inicio
	inicio = int(input("Ingrese la piscina donde quiere iniciar: "))
	# solicitamos el nodo objetivo
	meta = int(input("Ingrese la piscina a donde quiere llegar: "))
	#retornamos el nodo de inicio y de meta
	return inicio, meta


def mostrarEstadosPiscinas(estados):
	"""
 	Función que nos permite mostrar los estados de las piscinas ya sea que esté "Muy sucio" - "Poco sucio" - "Regular" - "Casi Limpio" - "Limpio"
	_____________
 	estado: lista que contiene el estado de cada piscina con respecto a la suciedad
  	Retorno
   	____________
	No retorna ningún valor
  	"""
	#Imprimimos mensaje piscinas sucias
	print("\nPiscinas más sucias")
	#bucle for que itera sobre cada elemento de la lista estados, asignando a j el índice del elemento actual y a estado su valor.
	for j, estado in enumerate(estados):
		#si el estado es 5
		if estado == 5:
			#Indicamos que la piscina está muy sucia
			print("Piscina:", j, " - Estado piscina: ", colored("Muy sucio", "red"))
		#si el estado es 4
		elif estado == 4:
			#Indicamos que la piscina está un poco sucia
			print("Piscina:", j, " - Estado piscina: ",
			      colored("Poco sucio", "light_red"))
		#si el estado es 3
		elif estado == 3:
			#Indicamos que la piscina está regular
			print("Piscina:", j, " - Estado piscina: ", colored("Regular", "yellow"))
		#si el estado es 2
		elif estado == 2:
			#Indicamos que la piscina está casi Limpia
			print("Piscina:", j, " - Estado piscina: ",
			      colored("Casi Limpio", "light_green"))
		#si el estado es 1
		else:
			#Indicamos que la piscina está Limpia
			print("Piscina:", j, " - Estado piscina: ", colored("Limpio", "cyan"))


def limpiarDesdePiscinaMasSucia(estados):
	"""
 	Función que nos permite cambiar el estado de la piscina de sucio a limpio
   	Parámetros
	_____________
 	estado: lista que contiene el estado de cada piscina con respecto a la suciedad
  	Retorno
   	____________
	No retorna ningún valor
  	"""
	#imprimimos que iniciamos con la limpieza
	print("\nComenzando limpieza...\n")
	#ciclo while que se ejecuta mientras el valor máximo en la lista de estados es mayor o igual a 2
	while max(estados) >= 2:
		#llamamos a la función "buscarNodosSucios", que devuelve una lista de nodos sucios
		nodosSucios = buscarNodosSucios(estados)
		#bucle for que itera a través de cada nodo en la lista de nodosSucios
		for nodo in nodosSucios:
			#imprimimos que nodo se está limpiando
			print(f"Limpiando nodo {nodo}...")
			#cambiamos el estado del nodo actual a 1, indicando que ha sido limpiado.
			estados[nodo] = 1


# Función para buscar los nodos más sucios
def buscarNodosSucios(estados):
	"""
 	Función que nos buscar los nodos (piscinas) más sucias del grafo
   	Parámetros
	_____________
 	estado: lista que contiene el estado de cada piscina con respecto a la suciedad
  	Retorno
   	____________
	nodosSucios: lista que contiene los nodos más sucios.
  	"""
	#lista vacia donde se almacenan los nodos con estado sucio
	nodosSucios = []
	#variable que al almacena el nodo más sucio
	nodoMasSucio = max(estados)
	#bucle for para iterar por todos los estados de las piscinas
	for i, estado in enumerate(estados):
		#validamos que si el estado del nodo es igual a Sucio
		if estado == nodoMasSucio:
			#añadimos ese nodo a la lista
			nodosSucios.append(i)
	#retornamos la lista con los nodos sucios
	return nodosSucios
