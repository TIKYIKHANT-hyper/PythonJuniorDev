import random
import time

start_time = time.time()
def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr



def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

testlist = [50,20,30,10,40,60]
result = bogo_sort(testlist)
print(result)
end_time = time.time()

total_time = end_time - start_time
print("Time taken:", total_time)