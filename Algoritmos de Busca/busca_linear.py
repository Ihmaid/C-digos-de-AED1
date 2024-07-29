def busca_linear(lista, valor):
    found = False
    indexs = []
    for pos, item in enumerate(lista):
        if item == valor:
            found = True
            indexs.append(pos)
        else:
            continue

    if found == False:
        return "Nada encontrado"

    return indexs


lista1 = [1, 34, 231, 45, 7, 645, 1, 3, 8, 0, 44, 133, 8]
print(busca_linear(lista1, 45))


