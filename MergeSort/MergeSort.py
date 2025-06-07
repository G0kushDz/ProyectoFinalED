import random

def mergeSort(arr):
    cont = [0]
    def _mergeSort(arr):
        if len(arr) > 1:
            cont[0] += 1
            mid = len(arr) // 2
            cont[0] += 2
            L = arr[:mid]
            R = arr[mid:]
            cont[0] += 2
            _mergeSort(L)
            _mergeSort(R)
            i = j = k = 0
            cont[0] += 3
            while i < len(L) and j < len(R):
                cont[0] += 1
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                    cont[0] += 3
                else:
                    arr[k] = R[j]
                    j += 1
                    cont[0] += 3
                k += 1
                cont[0] += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
                cont[0] += 3
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
                cont[0] += 3
    _mergeSort(arr)
    return cont[0]

conjuntos = [2, 10, 100, 1000, 10000]
print("\n°°° Merge Sort °°°")
for conjunto in conjuntos:
    tmp = [random.randint(1, 1000) for _ in range(conjunto)]
    pasos = mergeSort(tmp.copy())
    print(f"{conjunto} elementos... {pasos} pasos")
