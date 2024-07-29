def insertion_sort(list):
    n = len(list)

    if n < 2:
        return

    for i in range(1, n):
        key = list[i]
        j = i - 1
        while key < list[j] and j >= 0:
            list[j + 1] = list[j]
            j -= 1
            list[j + 1] = key

    return list


lista = [9, 3, 5, 1, 7]
lista2 = [5, 10, 2, 13, 4]
print(insertion_sort(lista))
