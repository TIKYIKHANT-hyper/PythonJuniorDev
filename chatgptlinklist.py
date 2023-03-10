class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data=data)
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(data=data)

    def insert(self, data):
        new_node = Node(data=data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def insert_anywhere(self, index, data):
        new_node = Node(data=data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        current_index = 0
        while current_node:
            if current_index == index - 1:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
            current_index += 1
        raise IndexError("Index out of range")

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
