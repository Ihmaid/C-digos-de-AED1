class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, info):
        node = Node(info)
        current = self.top
        if self.top is None:
            self.top = node
        else:
            while current.next:
                current = current.next
            current.next = node
