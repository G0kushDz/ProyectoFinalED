import random

def insertionSort(arr):
    cont = 0
    for j in range(1, len(arr)):
        cont += 2
        key = arr[j]
        cont += 1
        i = j - 1
        cont += 2
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            cont += 1
            i -= 1
            cont += 2
        arr[i + 1] = key
        cont += 1
    return cont

conjuntos = [2, 10, 100, 1000, 10000]
print("\n°°° Insertion Sort °°°")
for conjunto in conjuntos:
    tmp = [random.randint(1, 1000) for _ in range(conjunto)]
    pasos = insertionSort(tmp.copy())
    print(f"{conjunto} elementos... {pasos} pasos")
