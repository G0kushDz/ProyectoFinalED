import random

def quickSort(arr):
    cont = [0]
    def partition(arr, low, high):
        cont[0] += 1
        pivot = arr[high]
        cont[0] += 1
        i = low - 1
        cont[0] += 2
        for j in range(low, high):
            cont[0] += 1
            if arr[j] < pivot:
                i += 1
                cont[0] += 2
                arr[i], arr[j] = arr[j], arr[i]
                cont[0] += 3
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        cont[0] += 3
        return i + 1

    def _quickSort(arr, low, high):
        if low < high:
            cont[0] += 1
            pi = partition(arr, low, high)
            _quickSort(arr, low, pi - 1)
            _quickSort(arr, pi + 1, high)

    _quickSort(arr, 0, len(arr) - 1)
    return cont[0]

conjuntos = [2, 10, 100, 1000, 10000]
print("\n°°° Quick Sort °°°")
for conjunto in conjuntos:
    tmp = [random.randint(1, 1000) for _ in range(conjunto)]
    pasos = quickSort(tmp.copy())
    print(f"{conjunto} elementos... {pasos} pasos")
