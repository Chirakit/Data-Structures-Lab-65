"""Lab9.2 Selection Sort by Chirakit Marachchalee"""

def selectionSort(list, last):
    current = 0
    while (current <= last):
        smallest = current
        walker = current + 1
        while (list[walker] < list[smallest]):
            if walker < smallest:
                smallest = walker
            walker += 1
        list[current], list[smallest] = list[smallest], list[current]
        current += 1
        print(list)

selectionSort([23, 78, 45, 8, 32, 56], 5)
