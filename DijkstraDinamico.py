import heapq
import time
import matplotlib.pyplot as plt

def dijkstra(grafito, comienzo):
    dist = {node: float('infinity') for node in grafito}
    dist[comienzo] = 0
    xd = set()

    filapriori = [(0, comienzo)]

    while filapriori:
        diztAct, nodoAct = heapq.heappop(filapriori)

        if nodoAct in xd:
            continue
        xd.add(nodoAct)
        for vecinita, pesopesao in grafito[nodoAct].items():
            dizt = diztAct + pesopesao
            if dizt < dist[vecinita]:
                dist[vecinita] = dizt
                heapq.heappush(filapriori, (dizt, vecinita))
    return dist

def measure_time(grafito, comienzoNodo):
    inicioTiempo = time.time()
    dijkstra(grafito, comienzoNodo)
    cfinite = time.time()
    return cfinite - inicioTiempo

grafitoTamanio = list(range(10, 101, 10))

times = []
for size in grafitoTamanio:
    grafito = {str(i): {str(i+1): 1} for i in range(size - 1)}
    grafito[str(size - 1)] = {}
    comienzoNodo = '0'
    times.append(measure_time(grafito, comienzoNodo))

plt.plot(grafitoTamanio, times)
plt.title('Tiempo de ejecución del algoritmo de Dijkstra xdd')
plt.xlabel('Tamaño del grafo')
plt.ylabel('Tiempo en secondos')
plt.show()
