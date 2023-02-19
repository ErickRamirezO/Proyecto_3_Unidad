#libreria para usar las colas de prioridad
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


def busquedaAProfundidad(graph, start, end, estados, cost):
	"""
	Funcion que realiza la busqueda general desde el nodo de inicio hasta el nodo meta retornando el valor del costo por la busqueda realizada.
 	Parámetros
  	--------------------
   	grafo: grafo que está formado por una lista de listas
 	inicio: nodo desde donde se va a iniciar la búsqueda.
  	meta: nodo a donde se desea llegar.
    estados: diccionario de los estados de cada nodo
   	Retorno
   	--------------------
   	No retorna ningún valor
 	"""
	# Se crea una lista stack que contiene el nodo de inicio, una lista con solo ese nodo y un costo inicial de cero
	stack = [(start, [start], 0)]
    # Se define una variable para almacenar el nodo más sucio encontrado y otra para el costo total
	nodo_mas_sucio = None
	costo_total = 0
	# Mientras la lista stack tenga elementos, se ejecuta un bucle
	while stack:
        # Se toma el último elemento de la lista stack (el nodo), su camino y su costo actual
		vertex, path, cost_so_far = stack.pop()
        # Si el nodo actual no está en el estado, se salta a la siguiente iteración
		if vertex not in estados:
			continue
        # Si el nodo actual es más sucio que el nodo almacenado previamente, se actualiza el nodo y el costo total
		if nodo_mas_sucio is None or estados[vertex] > estados[nodo_mas_sucio]:
			nodo_mas_sucio = vertex
			costo_total = cost_so_far
        # Se recorren los vecinos del nodo actual
		for neighbor in graph[vertex]:
            # Se calcula el costo de moverse desde el nodo actual al vecino
			new_cost = cost.get((vertex, neighbor), 0)
            # Si el vecino no está en el camino y está en el estado y es más sucio que el nodo almacenado previamente,
            # se agrega el vecino, su camino actualizado y el costo total actualizado a la lista stack
			if neighbor not in path and neighbor in estados and estados[neighbor] > estados[nodo_mas_sucio]:
				stack.append((neighbor, path + [neighbor], cost_so_far + new_cost))

	#Imprimimos el nodo más sucio y el coste por la búsqueda
	print(f"El nodo más sucio es: {nodo_mas_sucio}")
	print(f"Costo por búsqueda: {costo_total}")

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