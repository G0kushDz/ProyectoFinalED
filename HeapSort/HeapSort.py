import random

def heapSort(arr):
    cont = [0]
    def heapify(arr, n, i):
        largest = i
        cont[0] += 1
        l = 2 * i + 1
        r = 2 * i + 2
        cont[0] += 2
        if l < n and arr[l] > arr[largest]:
            largest = l
            cont[0] += 2
        if r < n and arr[r] > arr[largest]:
            largest = r
            cont[0] += 2
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            cont[0] += 3
            heapify(arr, n, largest)

    n = len(arr)
    cont[0] += 1
    for i in range(n // 2 - 1, -1, -1):
        cont[0] += 1
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        cont[0] += 3
        heapify(arr, i, 0)
    return cont[0]

conjuntos = [2, 10, 100, 1000, 10000]
print("\n°°° Heap Sort °°°")
for conjunto in conjuntos:
    tmp = [random.randint(1, 1000) for _ in range(conjunto)]
    pasos = heapSort(tmp.copy())
    print(f"{conjunto} elementos... {pasos} pasos")
