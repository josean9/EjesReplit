"""Una restricción se expresa mediante un par (i,j) de números enteros comprendidos
 entre 1 y n, que indica que la tarea ti va antes que la tarea tj. Es decir, la tarea
  ti debe estar terminada antes de empezar la tarea tj. La relación binaria «... precede ...» 
  así definida en el conjunto de las n tareas es una relación de orden parcial: algunas tareas
   no son comparables.

1. Hacer un algoritmo que calcule una ordenación de la n tareas cumpliendo las restricciones.

Está claro que no se pueden cumplir todas las restricciones. En este caso, no hay ordenación 
de las tareas. El algoritmo deberá tratar este caso correctamente."""
resticciones = {(5,2),(5,0),(4,0),(4,1),(2,3),(3,1)} # de las restricciones pasamos a los numeros y sus vecinos
grafo = {0: [], 1: [], 2: [3], 3: [1], 4: [0, 1], 5: [2, 0]} #los numeros con sus vecinos
pila = [] #pila vacia en la que saldran los numeros ordenados
def ordenar(nodo): #funcion recursiva que va a ordenar los numeros
  for vecino in grafo[nodo]: 
    if vecino not in pila: 
      ordenar(vecino)
  pila.insert(0,nodo)
def main(): #funcion principal 
  for nodo in grafo: 
    if nodo not in pila: #si el nodo no esta todavia en la pila, se inicia la funcion recursiva
      ordenar(nodo)  
  print(pila)
print(main())