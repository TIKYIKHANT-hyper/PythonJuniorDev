def binary_search(listdata ,target):
    if len(listdata) == 0:
        return False
    else:
        midpoint = len(listdata)//2

    if listdata[midpoint] == target:
        return midpoint
    elif listdata[midpoint] < target:
        return binary_search(listdata[midpoint+1:],target)
    else:
        return binary_search(listdata[:midpoint],target)

testcase = [1,2,3,4,5,6,7,8,9,10]
res = binary_search(testcase,12)
print(res)