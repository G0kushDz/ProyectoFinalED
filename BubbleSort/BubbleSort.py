import random

def bubbleSort(arr):
    cont = 0
    for i in range(len(arr)):
        cont += 1
        for j in range(0, len(arr) - i - 1):
            cont += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                cont += 3
    return cont

conjuntos = [2, 10, 100, 1000, 10000]
print("\n°°° Bubble Sort °°°")
for conjunto in conjuntos:
    tmp = [random.randint(1, 1000) for _ in range(conjunto)]
    pasos = bubbleSort(tmp.copy())
    print(f"{conjunto} elementos... {pasos} pasos")
