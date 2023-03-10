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
        while current:
            count += 1
            current = current.next_node

        return count

    def add(self,data):
        new_node = node(data)
        new_node.next_node = self.header
        self.header = new_node

    def __repr__(self):
        linklist = []
        current = self.header

        while current:
            if current == self.header:
                linklist.append(f"[Head:{current.data}]")
            elif current.next_node ==  None:
                linklist.append(f"[Tail:{current.data}]")
            else:
                linklist.append(f"{current.data}")

            current = current.next_node

        return "-> ".join(linklist)
