class Node:
    """ A singly-linked node. """
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
    def __init__ (self):
        self.tail = None
        self.head = None
        self.size = 0
        
    def append(self, data):
        # Encapsulate the data in a Node 
        node = Node(data)
        if self.head is None:
            self.head = node    
        else: 
            current = self.head 
            while current.next:
                current = current.next 
            current.next = node

    def append_at_a_location(self, data, index):  
        current = self.head  
        prev = self.head  
        node = Node(data) 
        if self.head is None or index <= 0:
            self.head = Node(data)
        else:
            # Search for node at position index - 1 or the last position
            probe = self.head
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1
            # Insert new node after node at position index - 1
            # or last position
            node.next = probe.next
            probe.next = node#, probe.next)
            
words = SinglyLinkedList()
words.append('1 fatia de pão')
words.append('1 fatia de presunto')
words.append('1 fatia de queijo')
words.append('1 fatia de pão')

current = words.head
while current:
    print(current.data)
    current = current.next

#words.append('1 fatia de pão torrado')    
words.append_at_a_location('1 fatia de mortadela', 1)

print()
current = words.head
while current:
    print(current.data)
    current = current.next
    

