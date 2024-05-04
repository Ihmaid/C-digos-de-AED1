class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self, info):
        node = Node(info)
        current = self.head
        if self.head is None:
            self.head = node
        else:
            while current.next:
                current = current.next
            current.next = node

    def dequeue(self):
        prox = self.head.next
        self.head = prox

    def list(self):
        current = self.head
        while current:
            print(current.info)
            current = current.next


fila = Queue()
fila.enqueue('Gabriel')
fila.enqueue('Alice')
fila.enqueue('Samira')
fila.list()
fila.dequeue()
fila.list()
