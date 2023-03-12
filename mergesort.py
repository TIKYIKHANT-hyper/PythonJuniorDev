def merge_sort(listdata):

    if len(listdata) <= 1:
        return listdata

    midpoint = len(listdata) // 2
    leftdata = listdata[:midpoint]
    rightdata = listdata[midpoint:]

    left = merge_sort(leftdata)
    right = merge_sort(rightdata)

    return merge(left,right)

def merge(a,b):
    i,j = 0,0
    n,m = len(a),len(b)
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result += a[i:]
    result += b[j:]

    return result

testlist = [9, 5, 7, 1, 3]

print(merge_sort(testlist))