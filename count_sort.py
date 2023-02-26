import random
from cal_time import *
import copy

@cal_time
def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count+1)]
    for val in li:
        count[val] +=1
    li.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)

@cal_time
def sys_sort(li):
    li.sort()

li = [random.randint(0,100) for _ in range(10000000)]
li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)

count_sort(li1)
sys_sort(li2)
