class node:
    data = None
    next_node = None
    def __init__(self,data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" %self.data

class linked_lists:
    def __init__(self):
        self.header = None

    def isEmpty(self):
        return self.header == None

    def size(self):
        count = 0
        current = self.header
        while current != None:
            count += 1
            current = current.next_node

        return count