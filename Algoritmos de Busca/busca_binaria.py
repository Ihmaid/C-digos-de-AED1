def busca_binaria(lista, valor):
    n = len(lista)
    min = 0
    max = n - 1
    while min <= max:
        chute = round((min + max) / 2)
        if valor == lista[chute]:
            return chute
        elif valor > lista[chute]:
            min = chute + 1
        elif valor < lista[chute]:
            max = chute - 1

    return "Nada encontrado"


lista1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
print(busca_binaria(lista1, 10))
