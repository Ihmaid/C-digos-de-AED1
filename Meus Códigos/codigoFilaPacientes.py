class Paciente:
    def __init__(self, nome = None):
        self.nome = nome
        self.next = None

class FilaPaciente:
    #contador = 0

    def __init__(self):
        self.head = None

    def enqueue(self, nome):
        paciente = Paciente(nome)

        atual = self.head
        if self.head == None:
            self.head = paciente
        else:
            while atual.next != None:
                atual = atual.next
            atual.next = paciente

        #contador += 1

    def dequeue(self):
        atual = self.head
        if self.head is None:
            print("A fila está vazia!")
        else:
            self.head = atual.next

        #contador -= 1
            
    def getsize(self):
        atual = self.head
        contador = 0
        while atual:
            atual = atual.next
            contador += 1
        print("Quantidade de elementos da lista: ",contador)
         

def listar(fila):
    atual = fila.head
    print("Fila: ")
    if atual is None:
        print("Fila vazia!")
    while atual:
        print(atual.nome, end = ", ")
        atual = atual.next
    print()

fila1 = FilaPaciente()
while True:
    print()
    print("Escolha sua opção: ")
    print("1- Enqueue")
    print("2- Dequeue")
    print("3- Tamanho da lista")
    print("Q- Sair")

    escolha = input("Opção escolhida: ")

    if escolha == "1":
        nome = input("Nome do Paciente: ")
        fila1.enqueue(nome)
        listar(fila1)
    elif escolha == "2":
        nome = fila1.dequeue()
        print("Retirado: ", nome)
        listar(fila1)
    elif escolha == "3":
        fila1.getsize()
    elif escolha in ["Q","q"]:
        break
    else:
        print("\t\t Escolha errada")
    

              
    

    