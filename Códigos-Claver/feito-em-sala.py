# não foi finalizado
class Nó:
    def __init__(self):
        self.info = None
        self.prox= None

class ListaLinkada :
    def __init__(self):
        self.ini = None

        self.primeiro_nó = Nó()
        self.segundo_nó = Nó()
        self.primeiro_nó.info = "VAsco"
        self.segundo_nó.info = "vasco"

        self.primeiro_nó.prox = self.segundo_nó

minhaLista = ListaLinkada()
print(minhaLista.primeiro_nó)
print("info = ", minhaLista.primeiro_nó.info)
print("prox = ",minhaLista.primeiro_nó.prox)

print("info = ", minhaLista.segundo_nó.info)