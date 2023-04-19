"""Lab9.3 Bubble Sort by Chirakit Marachchalee"""

def bubbleSort(list, last):
    current = 0
    sorted = False
    comparison = 0
    while (current <= last) and (sorted is False):
        walker = last
        sorted = True
        while walker > current:
            comparison += 1
            if list[walker] < list[walker - 1]:
                sorted = False
                list[walker], list[walker - 1] = list[walker - 1], list[walker]
            walker -= 1
        current += 1
        print(list)
    print("Comparison times:", comparison)

#bubbleSort([23, 78, 45, 8, 32, 56], 5)
#bubbleSort([2, 1, 3, 4, 5, 6], 5)
#bubbleSort([503, 87, 512, 61, 908, 170, 897, 275, 653, 426, 154, 765, 703], 12)
