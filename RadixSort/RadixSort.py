import random

def radixSort(arr):
    cont = 0

    def counting_sort_exp(arr, exp):
        nonlocal cont
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        cont += 2 + 10

        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1
            cont += 3

        for i in range(1, 10):
            count[i] += count[i - 1]
            cont += 2

        i = n - 1
        while i >= 0:
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1
            cont += 5

        for i in range(n):
            arr[i] = output[i]
            cont += 2

    if not arr:
        return cont

    max_val = max(arr)
    cont += len(arr)

    exp = 1
    while max_val // exp > 0:
        counting_sort_exp(arr, exp)
        exp *= 10
        cont += 2

    return cont

conjuntos = [2, 10, 100, 1000, 10000]
print("\n°°° Radix Sort °°°")
for conjunto in conjuntos:
    tmp = [random.randint(1, 10) for _ in range(conjunto)]
    pasos = radixSort(tmp.copy())
    print(f"{conjunto} elementos... {pasos} pasos")
