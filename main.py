class node:
    def __init__(self, id, next):
        self.id = id
        self.next = next

    def __repr__(self):
        return f"Object code as {self.id} indicates {self.next}"
class structure:
    def __init__(self):
        self.header = None

    def size(self):
        count = 0
        while self.header != None:
            count += 1
        return count
    def adder(self,data):
        new_node = node(data,self.header)
        self.header = new_node

testcase1 = structure()
data1 = node(1,None)
testcase1.header = data1
data2 = node(2,None)
testcase1.adder(data2)
print(data1)
print(testcase1)