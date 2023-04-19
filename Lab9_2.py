"""Lab9.2 Selection Sort by Chirakit Marachchalee"""

def selectionSort(list, last):
    current = 0
    comparison = 0
    while current <= last:
        smallest = current
        walker = current + 1
        while walker <= last:
            if list[walker] < list[smallest]:
                smallest = walker
            walker += 1
            comparison += 1
        list[current], list[smallest] = list[smallest], list[current]
        current += 1
        print(list)
    print("Comparison times:", comparison)

#selectionSort([23, 78, 45, 8, 32, 56], 5)
#selectionSort([2, 1, 3, 4, 5, 6], 5)
#selectionSort([503, 87, 512, 61, 908, 170, 897, 275, 653, 426, 154, 765, 703], 12)
