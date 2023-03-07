def binary_search(listdata,target):
    start = 0
    end = len(listdata)-1
    while start <= end:
        midpoint = (start + end) //2
        if listdata[midpoint] == target:
            return midpoint
        elif listdata[midpoint] < target:
            start = midpoint + 1
        else:
            end = midpoint
    return False

testcase = [1,2,3,4,5,6,7,8]
result = binary_search(testcase,4)
result1 = binary_search(testcase,13)
print(result)
print(result1)

