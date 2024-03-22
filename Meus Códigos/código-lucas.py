class No:
    def __init__(self,valor):
        self.info = valor
        self.prox = None

class ListaLinkada:
    def __init__(self):
        self.ini = None
        self.tamanho = 0

    def adicionar(self,el):
        no = No(el)
        if self.ini is None:
            self.ini = no
        else:
            atual = self.ini
            while (atual.prox): #Enquanto atual.prox existir a estrutura vai loopar
                atual=atual.prox
            atual.prox = no

        self.tamanho += 1 #Incrementa a quantidade de elemento da lista

    def __len__(self):
        return self.tamanho
    
    def __getitem__(self, index):
        atual = self.ini
        for i in range(index):
            if atual:
               atual = atual.prox
            else:
                raise IndentationError("list index out of range")
            
    # def modify(self, index, el):
        # atual = self.ini
        # for i in range(index):
            # if atual:
                # atual = atual.prox
            # else:
                # raise IndentationError("list index out of range")
        # if atual:
            # atual.valor = el
        # else: 
                # raise IndentationError("list index out of range")  

    def modify(self, index, elem):
        if(self.ini is None):
            raise IndentationError("A lista está vazia")
        elif (self.tamanho < index):
            raise IndentationError("Não possui numero na posição passada")
        else:
            current = self.ini
            aux = 1
            while(aux < index):
                current = current.prox
                aux += 1
            current.data = elem      

ingredientes = ListaLinkada()
ingredientes.adicionar("Pão")
ingredientes.adicionar("Queijo")
ingredientes.adicionar("Presunto")
ingredientes.adicionar("Pão")

ingredientes.modify(1, "vasco")


current = ingredientes.ini
while current:
    print(current.info)
    current = current.prox


