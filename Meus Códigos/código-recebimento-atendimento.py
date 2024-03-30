class Pessoa:
    def __init__(self,value):
        self.nome = value
        self.next = None

class Fila:
    def __init__(self):
        self.head = None

    def receber(self,value):
        cliente = Pessoa(value)

        if self.head is None:
            self.head = cliente
        else:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next 
            pointer.next = cliente


    def atender(self):
        pointer = self.head
        print("Sendo atendido:",pointer.nome)
        self.head = pointer.next
        

filaDeClientes = Fila()

opcao = 0
while(opcao != 4):

    print("\nO que deseja fazer:\n1-Recebimento\n2-Atendimento\n3-Imprimir lista\n4-Encerrar programa\n")
    opcao = int(input())
    if opcao == 1:
        print("Nome do cliente\n")
        nome = input()
        filaDeClientes.receber(nome)
    elif opcao == 2:
        filaDeClientes.atender() 
    elif opcao == 3:
        pointer = filaDeClientes.head
        while(pointer):
            print(pointer.nome)
            pointer = pointer.next
