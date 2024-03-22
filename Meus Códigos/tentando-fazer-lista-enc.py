class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = node

    def prepend(self,value):
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            pointer = self.head
            self.head = node
            node.next = pointer

    # DESAFIO - Criar função para inserir um item no meio da lista
            
    # def insert(self,index,value):

list = LinkedList()
list.append("Gabriel")
list.append("Ama")
list.append("Alice <3")
list.prepend("O")

pointer = list.head
while(pointer):
    print(pointer.data)
    pointer = pointer.next
