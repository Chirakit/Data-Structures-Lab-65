"""Lab9.1 Insertion Sort by Chirakit Marachchalee"""

def insertionSort(list, last):
    current = 1
    comparison = 0
    while current <= last:
        hold = list[current]
        walker = current - 1
        comparison += 1
        while walker >= 0 and hold < list[walker]:
            list[walker + 1] = list[walker]
            walker -= 1
            comparison += 1
        list[walker + 1] = hold
        current += 1
        if walker < 0:
            comparison -= 1
        print(list)
    print("Comparison times:", comparison)

#insertionSort([23, 78, 45, 8, 32, 56], 5)
#insertionSort([2, 1, 3, 4, 5, 6], 5)
#insertionSort([503, 87, 512, 61, 908, 170, 897, 275, 653, 426, 154, 765, 703], 12)
