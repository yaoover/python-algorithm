import random
from cal_time import *

@cal_time
def bubble_sort(li):
    for i in range(len(li)-1):
        exchange = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        # print(li)
        if not exchange:
            return


# li = [random.randint(0,10000) for i in range(100)]
# li = [9,8,7,1,2,3,4,5,6]
li = list(range(10000))
random.shuffle(li)
# print(li)
bubble_sort(li)
