#libreria para usar las colas de prioridad
import heapq


def busquedaTodasLasRutasPosibles(grafo, costo, inicio, meta):
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
   	No retorna ningún valor
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
					lista.append(
					 (vecino, ruta + [vecino], costo_actual + costo[(nodo, vecino)]))

# Imprime cada ruta y su costo encontrado.
	for ruta, costo in rutas:
		print("Ruta:", ruta, "Costo:", costo)

def busquedaAnchura(grafo, inicio, objetivo, costo):
	"""
    Realiza la búsqueda por anchura desde el nodo de inicio hasta el nodo meta,
    y encuentra el nodo más sucio de una lista.

    Parametros:
    - graph: grafo que está formado por una lista de listas
    - start: nodo de inicio.
    - end: nodo meta.
    - cost: diccionario que representa el costo de ir desde un nodo a otro.

    Retorno:
    - No retorna ningún valor
    """
    # se usa una cola para almacenar los nodos que se deben visitar
    # una lista de tuplas que contiene el nodo actual y la ruta hasta el nodo actual
    # se almacenan los nodos ya visitados
	cola = [(inicio, [inicio])]  
	visitados = set()
 
    # se sigue buscando mientras haya nodos por visitar en la cola
	while cola:
        # se saca el primer elemento de la cola
		(nodo, ruta) = cola.pop(0)
        # si el nodo no ha sido visitado, se marca como visitado
		if nodo not in visitados:
            # se agregan los nodos adyacentes a la cola y se actualiza la ruta
			for adyacente in grafo[nodo]:
				#si el nodo adyacente es igual al objetivo entonces...
				if adyacente == objetivo:
					#añadimos ese nodo a la ruta
					ruta.append(objetivo)
                    # se imprime la ruta más corta y el costo total
					print(f"Ruta más corta: {ruta}")
					print(f"Costo total: {costo[(nodo, adyacente)] + sum(costo[(ruta[i], ruta[i+1])] for i in range(len(ruta)-1))}")
					#termina la función
					return
				#caso contrario
				else:
					cola.append((adyacente, ruta + [adyacente]))
            # se marca el nodo actual como visitado
			visitados.add(nodo)
 
    # si no se encuentra una ruta, se imprime un mensaje de error
	print("No se encontró una ruta")


def busquedaAProfundidad(graph, start, end, cost):
	"""
    Realiza la búsqueda a profundidad desde el nodo de inicio hasta el nodo meta,
    y encuentra el nodo más sucio de una lista.

    Parametros:
    - graph: grafo que está formado por una lista de listas
    - start: nodo de inicio.
    - end: nodo meta.
    - cost: diccionario que representa el costo de ir desde un nodo a otro.

    Retorno:
    - No retorna ningún valor
    """
	# Se crea una lista stack que contiene el nodo de inicio, una lista con solo ese nodo y un costo inicial de cero
	stack = [(start, [start], 0)]
	# Se define una variable para almacenar el nodo más sucio encontrado y otra para el costo total
	ruta = []
	costo_total = 0

	# Mientras la lista stack tenga elementos, se ejecuta un bucle
	while stack:
		vertex, path, cost_so_far = stack.pop()
		if vertex == end:
			ruta = path
			costo_total = cost_so_far
			break
		for neighbor in graph[vertex]:
			new_cost = cost.get((vertex, neighbor), 0)
			# Si el vecino no está en el camino y es más sucio que el actual nodo más sucio,
			# se añade a la pila para ser explorado más tarde.
			if neighbor not in path:
				stack.append((neighbor, path + [neighbor], cost_so_far + new_cost))

	#Imprimimos el nodo más sucio y el coste por la búsqueda
	print(f"La ruta para llegar desde el nodo {start} al nodo {end}: {ruta}")
	print(f"Costo: {costo_total}")


def dijkstra(graph, start, end, cost):
	"""
    Función que implementa el algoritmo de Dijkstra para encontrar el camino más corto
    desde un nodo de inicio hasta un nodo meta.

    Args:
    - graph: grafo que está formado por una lista de listas
    - start: nodo de inicio.
    - end: nodo meta.
    - cost: diccionario que representa el costo de ir desde un nodo a otro.

    Returns:
    - El costo total de la ruta más corta y la lista de nodos visitados para llegar desde el nodo de inicio al nodo meta.
    """
	# Inicialización de variables
	queue = [(0, start, [])]
	# Los nodos visitados se registran en un conjunto para evitar repetidos
	visited = set()
	# Algoritmo de Dijkstra
	while queue:
		(cost_so_far, vertex, path) = heapq.heappop(queue)
		if vertex in visited:
			continue
		visited.add(vertex)
		path = path + [vertex]
		if vertex == end:
			print("Ruta más corta encontrada:", path)
			print("Costo total:", cost_so_far)
			return
		for neighbor in graph[vertex]:
			new_cost = cost.get((vertex, neighbor), float('inf'))
			if neighbor not in visited:
				heapq.heappush(queue, (cost_so_far + new_cost, neighbor, path))

	print("No se encontró ninguna ruta desde", start, "hasta", end)