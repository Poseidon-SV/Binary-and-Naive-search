# BINARY SEARCH

# from typing import BinaryIO
# l=[6,4,7,3,9,5,8,5,9,7]
# s_l=sorted(set(l))


import time
import random

def naive_search(l,target):
    for i in range(len(l)):
        if l[i]==target:
            return i
    return -1


def binary_search(l, target, low=None, high=None ):
    for i in range(len(l)):
        if low is None:
            low=0
        if high is None:
            high=len(l)-1
        if high<low:
            return -1
        
        midPoint=(low+high)//2
        if l[midPoint]==target:
            return midPoint
        elif target<l[midPoint] :
            return binary_search(l, target, low, midPoint-1)
        elif target>l[midPoint]:
            return binary_search(l,target, midPoint+1,high)

# l=[2,4,5,6,8,9]
# target=6
# print(naive_search(l,target))          
# print(bianary_search(l,target))

length =1000
# build a sort list of length of 1000
sorted_list=set()
while len(sorted_list)<length:
    sorted_list.add(random.randint(-5*length,5*length))
sorted_list=sorted(list(sorted_list))

start = time.time()
for target in sorted_list:
    naive_search(sorted_list,target)
end = time.time()
print("Naive search time is ",(end-start)/length," second")

start = time.time()
for target in sorted_list:
    binary_search(sorted_list,target)
end = time.time()
print("Binary search time is ",(end-start)/length," seconds")

