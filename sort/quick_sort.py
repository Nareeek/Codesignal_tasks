# 1
from datetime import datetime
import timeit, time



def quickSort(a, l, r):
    if l >= r:
        return a

    x = a[l]  # barrier element
    i = l
    j = r

    while i <= j:
        while a[i] < x:
            i += 1
        while a[j] > x:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]

            i += 1
            j -= 1

    quickSort(a, l, j)
    quickSort(a, i, r)

    return a


print("start")
start_time = time.clock()
start1 = timeit.default_timer()
start2 = datetime.now()

quickSort(list(range(10000))[10000:5000:-2], 0, len(list(range(10000))[1000:5000:2]) - 1)

stop1 = timeit.default_timer()
stop2 = datetime.now() - start2

print('Time1: ', stop1 - start1) 
print('Time2: ', stop2)

print(time.clock() - start_time, " :seconds")

print("end")


# 2
def quick_sort(sequence):
    length = len(sequence)
    
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    
    items_greater = []
    items_lower = []
    
    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        
        else:
            items_lower.append(item)
            
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print("start")
quick_sort(list(range(10000))[::-1])
print("end")