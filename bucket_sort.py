import random

def bucket_sort(li, n=100, max_num= 10000):
    buckets = [[] for _ in range(n)]
    for var in li:
        i = min(var // (max_num //n), n-1)
        buckets[i].append(var)
        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1]  = buckets[i][j-1], buckets[i][j]
            else:
                break
    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)
    return sorted_li

li = [random.randint(0, 10000) for i in range(100000)]

bucket_sort(li)
print(li)