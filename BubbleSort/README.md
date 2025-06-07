°°° Bubble Sort °°°

Bubble Sort recorre la lista comparando pares de elementos adyacentes y, si están en el orden 
incorrecto, los intercambia. Este proceso se repite desde el inicio hasta el final de la lista, 
empujando los elementos más grandes hacia el final en cada pasada. En cada iteración, el algoritmo 
recorre la lista hasta el penúltimo elemento no ordenado, comparando de izquierda a derecha. 
Si un elemento es mayor que su siguiente, se realiza un intercambio. Después de cada pasada 
completa, el siguiente elemento más grande queda en su posición final. Este proceso se repite 
hasta que no se realicen más intercambios, lo que indica que la lista está ordenada.

°Tiempo de ordenamiento°
°Mejor caso: O(n)
 Esto ocurre cuando la lista ya está ordenada. Solo necesita una pasada para verificar que no se 
 requieren intercambios.

°Caso promedio: O(n²)
 Cuando los elementos están en un orden aleatorio. Se hacen múltiples comparaciones e intercambios.

°Peor caso: O(n²)
 Ocurre cuando la lista está en orden inverso. Cada elemento necesita moverse hasta el final, 
 requiriendo el máximo de comparaciones e intercambios posibles.


°Ventajas°
-Muy fácil de entender e implementar.
-No requiere memoria adicional.
-Útil para listas pequeñas o casi ordenadas.
-Puede detectar si la lista ya está ordenada y detenerse antes.

°Desventajas°
-Muy ineficiente para listas grandes debido a su complejidad cuadrática (O(n²)).
-Realiza muchas comparaciones e intercambios innecesarios en la mayoría de los casos.
-No es adecuado para aplicaciones que requieren alto rendimiento.



°° PROGRAMA: BubbleSort.py °°

Para comprobar su eficiencia se realizo un programa "BubbleSort.py" que se encuentra en la misma
carpeta que este archivo.
-El programa realiza el ordenamiento de 5 conjuntos cada uno con una cantidad diferente 
 de elementos, los elementos son generados de forma aleatoria:
	1er conjunto: 2 elementos
	2do conjunto: 10 elementos
	3er conjunto: 100 elementos
	4to conjunto: 1000 elementos
	5to conjunto: 10000 elementos


Estos fueron los resultados de una ejecución del programa, se muestra la cantidad de elementos que
se ordenaron y los pasos que tardó en realizar el ordenamiento:
2 elementos... 3 pasos
10 elementos... 127 pasos
100 elementos... 13708 pasos
1000 elementos... 1263526 pasos
10000 elementos... 125643244 pasos



La tabla siguiente representa una comparación de su eficiencia con otros algoritmos de ordenamiento
(Todos hicieron la prueba con los mismos 5 conjuntos):

		2 elementos	10 elementos	100 elementos	1,000 elementos	10,000 elementos
InsertionSort	( 7  )		( 72  )	 	( 5,147 )	( 502,197 )	( 50,028,401 )
BubbleSort	( 4  )		( 126 )		( 5,038 )	( 503,344 )	( 49,985,874 )
MergeSort	( 14 )		( 107 )		( 1,082 )	( 11,766  )	( 132,104    )
HeapSort	( 14 )		( 100 )		( 1,220 )	( 14,184  )	( 167,208    )
QuickSort	( 10 )		( 71  )		( 751   )	( 9,904   )	( 117,163    )
CountingSort	( 9  )		( 31  )		( 398   )	( 4,061   )	( 40,269     )
RadixSort	( 33 )		( 97  )		( 969   )	( 10,314  )	( 108,804    )
BucketSort	( 31 )		( 63  )		( 610   )	( 6,709   )	( 67,087     )
