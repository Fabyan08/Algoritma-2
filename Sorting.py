def bubble_sort(urutan):
    for _ in urutan:
        for j in range(len(urutan) - 1):
            if urutan[j] > urutan[j + 1]:
                urutan[j], urutan[j + 1] = urutan[j + 1], urutan[j]

data = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(data)
print(data)