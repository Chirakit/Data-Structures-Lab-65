"""Lab9.4 Sorting For Playing Cards by Chirakit Marachchalee"""

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

insertionSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)
#♣ < ♦ < ♥ < ♠