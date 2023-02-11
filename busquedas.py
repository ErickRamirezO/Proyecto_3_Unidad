import heapq
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
					lista.append(
					 (vecino, ruta + [vecino], costo_actual + costo[(nodo, vecino)]))

# Retorna la lista de rutas encontradas desde el nodo inicio hasta el nodo destino junto con sus costos.
	return rutas


def busquedaAProfundidad(graph, start, end):
	# Creación de una lista llamada stack que contiene el nodo de 			inicio y una lista con solo ese nodo
	stack = [(start, [start])]
	# Mientras la lista tenga elementos, se realiza un bucle
	while stack:
	# Se toma el último elemento de la lista (el nodo) y su camino hasta ese punto
		(vertex, path) = stack.pop()
	# Se recorren los vecinos del nodo actual
	for neighbor in graph[vertex]:
	# Si el vecino es el nodo de destino, se retorna el camino más el vecino
		if neighbor == end:
			return path + [neighbor]
		# Si no, se agrega el vecino y su camino actualizado a la lista
		else:
			stack.append((neighbor, path + [neighbor]))
	# Si no se encuentra un camino, se retorna None
	return None

def dijkstra(graph, start, end, costs):
    # La cola de prioridad contiene pares (costo, nodo, camino)
    queue = [(0, start, [start])]
    # Los nodos visitados se registran en un conjunto para evitar repetidos
    visited = set()
    while queue:
        # Obtener el nodo con el costo mínimo
        (cost, current_node, path) = heapq.heappop(queue)
        # Si el nodo actual no ha sido visitado
        if current_node not in visited:
            # Añadirlo a los visitados
            visited.add(current_node)
            # Si el nodo actual es el nodo final, devolver el camino y el costo
            if current_node == end:
                return (cost, path)
            # Revisar cada vecino del nodo actual
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    # Añadir el vecino a la cola de prioridad
                    # con el costo actualizado y el camino actualizado
                    heapq.heappush(queue, (cost + costs[(current_node, neighbor)], neighbor, path + [neighbor]))
    # Si no se encuentra un camino, devolver infinito y un camino vacío
    return (float("inf"), [])