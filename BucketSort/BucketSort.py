import random

def bucketSort(arr):
    cont = 0
    bucket_count = 10
    cont += 1
    max_val = max(arr)
    cont += len(arr)
    buckets = [[] for _ in range(bucket_count)]
    cont += bucket_count
    for num in arr:
        index = num * bucket_count // (max_val + 1)
        buckets[index].append(num)
        cont += 3
    i = 0
    for bucket in buckets:
        bucket.sort()
        for num in bucket:
            arr[i] = num
            i += 1
            cont += 3
    return cont

conjuntos = [2, 10, 100, 1000, 10000]
print("\n°°° Bucket Sort °°°")
for conjunto in conjuntos:
    tmp = [random.randint(1, 1000) for _ in range(conjunto)]
    pasos = bucketSort(tmp.copy())
    print(f"{conjunto} elementos... {pasos} pasos")
