from random import randint
import os
import time
b=[]
for i in range(100):
    b.append(randint(1,1000))
os.system('cls')
c=b.copy()
#Bubble sort
def bubble_sort(b):
    n=range(len(b))
    for i in n:
        for j in n:
            if b[i]<b[j]:
                b[i],b[j]= b[j],b[i]
    return b
start_time = time.perf_counter()
print(bubble_sort(b))
end_time = time.perf_counter()
print(f'{(end_time-start_time):.40f}')

b=c.copy()
# Quick sort
def quick_sort(a):
    if len(a)<=1:
        return a
    pivot=a[len(a)//2]
    left=[x for x in a if x<pivot]
    middle=[x for x in a if x==pivot]
    right=[x for x in a if x>pivot]
    return quick_sort(left)+middle+quick_sort(right)
start_time = time.perf_counter()
print(quick_sort(b))
end_time = time.perf_counter()
print(f'{(end_time-start_time):.40f}')
