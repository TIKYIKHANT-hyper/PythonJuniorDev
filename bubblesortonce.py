def bubblesort_once(l):
    newlist = list(l)
    for i in range(0,len(l)-1,1):
        if newlist[i] > newlist[i+1]:
            tempdata = newlist[i]
            newlist[i] = newlist[i+1]
            newlist[i+1] = tempdata
    return newlist



test1 = [9, 7, 5, 3, 1, 2, 4, 6, 8]
length = len(test1)
result = bubblesort_once(test1)
print(length)
print(result)
