import random

def countingSort(arr):
    cont = 0
    max_val = max(arr)
    cont += len(arr)
    count = [0] * (max_val + 1)
    cont += 1
    for num in arr:
        count[num] += 1
        cont += 2
    i = 0
    for num, freq in enumerate(count):
        cont += 1
        while freq > 0:
            arr[i] = num
            i += 1
            freq -= 1
            cont += 3
    return cont

conjuntos = [2, 10, 100, 1000, 10000]
print("\n°°° Counting Sort °°°")
for conjunto in conjuntos:
    tmp = [random.randint(1, 10) for _ in range(conjunto)]
    pasos = countingSort(tmp.copy())
    print(f"{conjunto} elementos... {pasos} pasos")
