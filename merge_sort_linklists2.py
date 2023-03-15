from linked_list import linked_lists
def merge_sort(arr):
    if arr == None or arr.next_node == None:
        return arr
    mid = getmiddle(arr)
    leftdata = arr
    rightdata = mid.next_node
    mid.next = None
    left = merge_sort(leftdata)
    right = merge_sort(rightdata)
    return merge(left,right)
def getmiddle(arr):
    midpoint = arr
    fullpoint = arr.next_node

    while midpoint != None and fullpoint != None:
        midpoint = midpoint.next_node
        fullpoint = fullpoint.next_node.next_node

    return midpoint

def merge(left,right):
    if left == None:
        return right
    elif right == None:
        return left

    if left.data <= right.data:
        result = left
        result.next_node = merge(left.next_node,right)
    else:
        result = right
        result.next_node = merge(left,right.next_node)

    return result