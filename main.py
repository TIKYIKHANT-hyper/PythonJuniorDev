class Node:
    def __init__(self,id,next = None):
        self.id = id
        self.next = next

    def __repr__(self):
        return f"object with ID :{self.id} indicating next {self.next}\n"

class linked_lists:
    def __init__(self , head):
        self.head = head
        self.__count = 0

    def add(self , id):
        current = self.head
        newNode = Node(id,self.head)
        self.head = current
        self.__count += 1

    def __len__(self):
        return self.__count+1

    def search(self , id):
        current = self.head
        while current:
            if current.id == id:
                return current
            else:
                current = current.next
        return None

data = Node(1)
storage1 = linked_lists(data)
storage1.add(2)
storage1.add(3)
n = storage1.search(3)
print(n)
