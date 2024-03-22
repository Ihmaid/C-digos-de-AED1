class Nó:                           # A classe está definindo o que os objetos irão ter de referência

    def __init__(self):             # Construtor da classe; No Python é obrigatório definir o construtor
                                        # pois não há construtor default
        self.info = None
        self.prox = None

class ListaEncadeadaSimples:
    def __init__ (self):
        self.ini = None             # Nesta classe, o único atributo do parâmetro será o ini
        
    def adicionar(self, item):
        nó = Nó()                   # Cria-se uma instância da classe Nó
        
        nó.info = item              # O atributo info do objeto nó da classe Nó recebe o valor do item que
                                        # será o parâmetro do método adicionar
        if self.ini is None:
            self.ini = nó           # Caso não haja um valor definido para ini, o nó será o ini. O ini é uma
                                        # referência, ou seja, é um ponteiro que aponta para o objeto nó
                                        # e recebe suas características 
        else: 
            atual = self.ini        # O valor inicial passa a ser o valor atual e a variável atual passa a
                                        # ser um objeto do tipo Nó

            while atual.prox:       # Enquanto o atual.prox existir, atual vai receber o valor de atual.prox.
                                        # O atual também é uma referência, ou seja, um ponteiro que recebe
                                        # as informações de self.ini
                atual = atual.prox      
            atual.prox = nó         
            
pals = ListaEncadeadaSimples()      # Cria-se uma instância da classe ListaEncadeadaSimples
pals.adicionar('pão')
pals.adicionar('queijo')
pals.adicionar('presunto')
pals.adicionar('pão')

atual = pals.ini
while atual:
    print(atual.info)
    atual = atual.prox
