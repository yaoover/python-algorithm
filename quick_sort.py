import random
from cal_time import *
import copy

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

def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left

def _quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        _quick_sort(li, left, mid-1)
        _quick_sort(li, mid+1, right)

@cal_time
def quick_sort(li):
    _quick_sort(li, 0, len(li)-1)

li = list(range(10000))
random.shuffle(li)

li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)

quick_sort(li1)
bubble_sort(li2)
print(li1)
print(li2)
