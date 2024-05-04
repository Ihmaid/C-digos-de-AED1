class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, info):
        node = Node(info)
        current = self.head
        if self.head is None:
            self.head = node
        else:
            while current.next:
                current = current.next
            current.next = node

    def append_at_location(self, info, index):
        current = self.head
        counter = 1
        node = Node(info)
        if self.head is None:
            self.head = node
        while current.next:
            if counter == index - 1:
                prox = current.next
                current.next = node
                node.next = prox
            current = current.next
            counter += 1

    def list(self):
        current = self.head
        while current:
            print(current.info)
            current = current.next


lista1 = LinkedList()
lista1.append('Gabriel')
lista1.append('Ama')
lista1.append('Alice')
lista1.append('teste')
lista1.append_at_location('Vasco', 3)
lista1.list()
