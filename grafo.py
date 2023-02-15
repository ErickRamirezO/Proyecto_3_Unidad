import networkx as nx
import random
import matplotlib.pyplot as plt
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
	#Imprimimos el nodo y el grafo en modo de lista de listas y en un diccionario para los costos
	#print(graph, cost)
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
	graph[8].append(9)#
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
	  8, 7)] = cost[(7, 16)] = cost[(16, 7)] = cost[(1, 2)] = cost[(2, 1)] = cost[(
	   1, 5)] = cost[(5, 1)] = cost[(2, 3)] = cost[(3, 2)] = cost[(3, 4)] = cost[(
	    4, 3)] = cost[(4, 5)] = cost[(5, 4)] = cost[(5, 6)] = cost[(
	     6, 5)] = cost[(6, 9)] = cost[(9, 6)] = cost[(6, 10)] = cost[(
	      10, 6)] = cost[(9, 11)] = cost[(11, 9)] = cost[(9, 8)] = cost[(
	       8, 9)] = cost[(8, 12)] = cost[(8, 13)] = cost[(8, 14)] = cost[(
	        8, 15)] = cost[(12, 8)] = cost[(13, 8)] = cost[(14, 8)] = cost[(
	         15, 8)] = cost[(16, 17)] = cost[(16, 18)] = cost[(16, 19)] = cost[(
	          16, 20)] = cost[(17, 16)] = cost[(18, 16)] = cost[(19, 16)] = cost[(20, 16)] = 2
	# creación de la lista de estados
	states = [random.randint(1, 5) for i in range(21)]
	
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
	G = nx.Graph()

	#Añadir nodos al grafo
	for i in range(21):
		G.add_node(i)

	#Añadir aristas al grafo
	for i in range(21):
		for j in grafo[i]:
			G.add_edge(i, j)

	#Visualización del grafo
	nx.draw(G, with_labels=True)
	plt.show()

def mostrarConexionesNodos(grafo,costo):
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
	inicio = int(input("Ingrese el nodo donde quiere iniciar: "))
	# solicitamos el nodo objetivo
	meta = int(input("Ingrese el nodo al que quiere llegar: "))
	return inicio,meta

def mostrarEstadosPiscinas(estados):
	print("\nPiscinas más sucias")
	for j, estado in enumerate(estados):
		if estado == 5:
			print("Piscina:", j, " - Estado piscina: ", colored("Muy sucio", "red"))
		elif estado == 4:
			print("Piscina:", j, " - Estado piscina: ", colored("Poco sucio", "light_red"))
		elif estado == 3:
			print("Piscina:", j, " - Estado piscina: ", colored("Regular", "yellow"))
		elif estado == 2:
			print("Piscina:", j, " - Estado piscina: ", colored("Casi Limpio", "light_green"))
		else:
			print("Piscina:", j, " - Estado piscina: ", colored("Limpio", "cyan"))


def limpiarDesdePiscinaMasSucia(estados):
	print("\nComenzando limpieza...\n")
	while max(estados) >= 2:
		nodosSucios = buscarNodosSucios(estados)
		for nodo in nodosSucios:
			print(f"Limpiando nodo {nodo}...")
			estados[nodo] = 1
	
	
# Función para buscar los nodos más sucios
def buscarNodosSucios(estados):
    nodosSucios = []
    nodoMasSucio = max(estados)
    for i, estado in enumerate(estados):
        if estado == nodoMasSucio:
            nodosSucios.append(i)
    return nodosSucios

	