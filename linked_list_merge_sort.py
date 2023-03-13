from linked_list import linked_lists

def merge_sort_list(data):
    if data.size() <= 1 or data == None:
        return data

    if data.header == None or data == None:
        lefthand = data
        righthand = None
        return lefthand,righthand
    else:
        middlepoint = data.size()//2
        midnode = data.nodeatIndex(middlepoint-1)
        lefthead = data
        righthead = data
        righthead.header == midnode.next_node
        midnode.next_node = None

        return lefthead,righthead