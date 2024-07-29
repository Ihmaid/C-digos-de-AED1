class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


# Uma função recursiva funciona com empilhamentos de chamadas da função.
# Exemplo de travessia de árvore: Travessia In Order
def in_order(root_node):
    current = root_node
    if current is None:
        return
    in_order(current.left_child)
    print(current.data, end=', ')
    in_order(current.right_child)


def pre_order(root_node):
    current = root_node
    if current is None:
        return
    print(current.data, end=', ')
    in_order(current.left_child)
    in_order(current.right_child)


def post_order(root_node):
    current = root_node
    if current is None:
        return
    in_order(current.left_child)
    in_order(current.right_child)
    print(current.data, end=', ')


nA = Node("A")
nB = Node("B")
nC = Node("C")
nD = Node("D")
nE = Node("E")

# Nós esquerdo e direito do Nó A
nA.right_child = nC
nA.left_child = nB

# Nós esquerdo e direito do Nó B e nós netos do nó A
nB.right_child = nE
nB.left_child = nD

in_order(nA)
print("\n")
pre_order(nA)
print("\n")
post_order(nA)
