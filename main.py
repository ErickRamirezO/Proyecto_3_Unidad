import networkx as nx
import matplotlib.pyplot as plt
def busqueda_general(grafo, costo, inicio, meta):
	"""
	Funcion que realiza la busqueda general desde el nodo de inicio hasta el nodo meta retornando el valor del costo por la busqueda realizada.
 	Parámetros
  	--------------------
   	grafo: grafo que está formado por una lista de listas
	costo: diccionario que contiene el costo de cada conexion de los nodos del grafo
 	inicio: nodo desde donde se va a iniciar la búsqueda.
  	meta: nodo a donde se desea llegar.
   	Retorno
   	--------------------
   	costo_actual: valor del costo obtenido al realizar la busqueda
	None: Si no se encuentra un camino desde el nodo de inicio hasta el nodo de destino
 	"""
	# Inicializa una lista vacía `rutas` para almacenar las rutas encontradas desde el nodo inicio hasta el nodo destino.
	rutas = []
    # Inicializa una lista "lista" con un solo elemento que es una tupla que contiene el nodo de inicio, una lista con el nodo inicio y un costo de 0.
	lista = [(inicio, [inicio], 0)]
    # Inicia un bucle while con la condición cola que ejecuta las siguientes operaciones mientras la cola no esté vacía.
	while lista:
        # Asigna a las variables nodo, ruta y costo_actual los valores del último elemento de la lista cola y lo elimina de la misma.
		nodo, ruta, costo_actual = lista.pop(0)
        # Verifica si nodo es igual a la meta deseada, si es así, agrega la ruta actual y su costo a la lista de rutas.
		if nodo == meta:
			rutas.append((ruta, costo_actual))
        # Si el nodo actual no es el destino, agrega a la cola todos los vecinos del nodo actual que aún no estén en la ruta actual.
		else:
			for vecino in grafo[nodo]:
				if vecino not in ruta:
					lista.append((vecino, ruta + [vecino], costo_actual + costo[(nodo, vecino)]))
    # Retorna la lista de rutas encontradas desde el nodo inicio hasta el nodo destino junto con sus costos.
	return rutas

def anchura():
	pass

def creacionGrafo():
	pass

if __name__ == "__main__":
	# creación del grafo y diccionario de costos
	graph,cost = [[] for i in range(21)],{}
	#Imprimimos el nodo y el grafo en modo de lista de listas y en un diccionario para los costos
	#print(graph, cost)
	# añadir los nodos
	#Piscina al aire libre -> 1
	#Agua relajante -> 2
	#Agua Terapéutica -> 3
	#Piscina semicubierta -> 4
	#Piscina cubierta -> 5
	#Aguas Termales -> 6
	#Hidromasaje -> 7
	#Agua de los pequeños -> 8 
	#Piscina Polar -> 9
	#Sauna -> 10
	#Turco -> 11
	#Ludicotermal -> 12
	#Caliente -> 13
	#Tibia -> 14
	#Fria -> 15
	#Salada -> 16
	#Piscina de olas -> 17 
	#Aguas Mixtas -> 18
	#Familiar -> 19
	#Parque acuático -> 20
	#Chapoteo -> 21
	#1 a 8
	graph[1].append(8)
	graph[8].append(1)
	#1 a 9
	graph[1].append(9)
	graph[9].append(1)
	#8 a 2
	graph[8].append(2)
	graph[2].append(8)
	#8 a 17
	graph[8].append(17)
	graph[17].append(8)
	#8 a 9
	graph[8].append(9)
	graph[9].append(8)
	#8 a 7
	graph[8].append(7)
	graph[7].append(8)
	#2 a 3
	graph[2].append(3)
	graph[3].append(2)
	#2 a 6
	graph[2].append(6)
	graph[6].append(2)
	#3 a 4
	graph[3].append(4)
	graph[4].append(3)
	#4 a 5
	graph[4].append(5)
	graph[5].append(4)
	#5 a 6
	graph[5].append(6)
	graph[6].append(5)
	#6 a 7
	graph[6].append(7)
	graph[7].append(6)
	#7 a 11
	graph[7].append(11)
	graph[11].append(7)
	#7 a 10
	graph[7].append(10)
	graph[10].append(7)
	#10 a 12
	graph[10].append(12)
	graph[12].append(10)
	#7 a 10
	graph[7].append(10)
	graph[10].append(7)
	#10 a 9
	graph[10].append(9)
	graph[9].append(10)
	#9 a 13,14,15,16
	graph[9].append(13)
	graph[9].append(14)
	graph[9].append(15)
	graph[9].append(16)
	graph[13].append(9)
	graph[14].append(9)
	graph[15].append(9)
	graph[16].append(9)
	#17 a 18,19,20,21
	graph[17].append(18)
	graph[17].append(19)
	graph[17].append(20)
	graph[17].append(21)
	graph[18].append(17)
	graph[19].append(17)
	graph[20].append(17)
	graph[21].append(17)

    # añadiendo el costo a los nodos, todos con el valor de 2
	cost[(1, 8)] = cost[(1, 0)] = cost[(1, 4)]= cost[(4, 1)]= cost[(0, 1)]= cost[(1, 8)]= cost[(8, 1)]= cost[(4, 5)]= cost[(5, 4)]= cost[(4, 7)]= cost[(7, 4)]= cost[(5, 3)]= cost[(3, 5)]= cost[(7, 2)]= cost[(2, 7)]= cost[(2, 3)]= cost[(3, 2)]= cost[(2, 6)]= cost[(6, 2)]= cost[(6, 8)]= cost[(8, 6)]= cost[(6, 3)]= cost[(3, 6)]= cost[(3, 8)]= cost[(8, 3)] = 2
	
	#Imprimimos el nodo y el grafo en modo de lista de listas y en un diccionario para los costos
	#print(graph, cost)
	# solicitamos el nodo objetivo
	G = nx.Graph()

	#Añadir nodos al grafo
	for i in range(21):
	    G.add_node(i)
	
	#Añadir aristas al grafo
	for i in range(21):
	    for j in graph[i]:
	        G.add_edge(i, j)
	
	#Visualización del grafo
	nx.draw(G, with_labels=True)
	plt.show()
	meta = int(input("Ingrese el nodo al que quiere llegar: "))
	
	# solicitamos nodo inicio
	inicio = int(input("Ingrese el nodo donde quiere iniciar: "))
	# Ejecuta la función `buscar_rutas` y asigna el resultado a la variable `rutas`.
	rutas = busqueda_general(graph, cost, inicio, meta)
	print(rutas)
	# Imprime cada ruta y su costo encontrado.
	for ruta, costo in rutas:
	    print("Ruta:", ruta, "Costo:", costo)

