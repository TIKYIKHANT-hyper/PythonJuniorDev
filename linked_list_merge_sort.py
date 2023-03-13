from linked_list import linked_lists

def merge_sort_list(data):
    if data.size() == 1 or data == None:
        return data
    left_half , right_half = split(data)
    left = merge_sort_list(left_half)
    right = merge_sort_list(right_half)
    return merge(left,right)
def merge(a,b):
    newlist = linked_lists()
    newlist.add(0)
    current = newlist.header
    left = a.header
    right = b.header
    while left or right:
        if left == None:
            current.next_node = right
            right = right.next_node
        elif right == None:
            current.next_node = left
            left = left.next_node
        else:
            left_data = left.data
            right_data = right.data
            if left_data < right_data:
                current.next_node = left
                left = left.next_node
            else:
                current.next_node = right
                right = right.next_node
        current = current.next_node

    head = newlist.header.next_node
    newlist.header = head
    return newlist

def split(data):
    if data.header == None or data == None:
        lefthand = data
        righthand = None
        return lefthand,righthand
    else:
        middlepoint = (data.size())//2
        midnode = data.nodeatIndex(middlepoint-1)
        lefthead = data
        righthead = linked_lists()
        righthead.header = midnode.next_node
        midnode.next_node = None

    return lefthead,righthead

l = linked_lists()
l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(200)
print(l)
sorted_list = merge_sort_list(l)
print(sorted_list)