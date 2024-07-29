def bubble_sort(list):
    n = len(list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            temp = list[j]
            if list[j] > list[j + 1]:
                list[j] = list[j + 1]
                list[j + 1] = temp

    return list


lista = [9, 3, 5, 1, 7]
lista2 = [5, 10, 2, 13, 4]
print(bubble_sort(lista))
