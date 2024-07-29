def selection_sort(list):
    for i in range(len(list) - 1):
        min_index = i
        for j in range(i, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        if list[i] > list[min_index]:
            aux = list[i]
            list[i] = list[min_index]
            list[min_index] = aux

    return list


lista = [9, 3, 5, 1, 7]
lista2 = [5, 10, 2, 13, 4]
print(selection_sort(lista))
