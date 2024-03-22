class Node:
    def __init__(self):
        self.data = None
        self.next = None

class ListaLinkada:
    def __init__(self):
        self.head = None

    # def adicionarNoFim(self, item):
    #     nó = Node()
    #     nó.dado = item
    #     if self.head is None:
    #         self.head = nó
    #     else:
    #         ponteiro = self.head
    #         while(ponteiro.proximo):
    #             ponteiro = ponteiro.proximo
    #         ponteiro.proximo = nó

    def adicionaNoInicio(self, item):
        # 1° cenário -> lista vazia como nasceu
        # 2° cenário -> lista com algum elemento
        nó = Node()
        nó.data = item
        if self.head is None:
            self.head = nó
        else:
            ponteiro = self.head
            nó.next = ponteiro
            self.head = nó


aux = ListaLinkada()
aux.adicionaNoInicio("vasco")
aux.adicionaNoInicio("gama")

ponteiro = aux.head
while(ponteiro):
    print(ponteiro.data)
    ponteiro = ponteiro.next