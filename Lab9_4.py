"""Lab9.4 Sorting For Playing Cards by Chirakit Marachchalee"""

def insertionSort(deck, last):
    current = 0
    comparison = 0
    for i in range(1, last+1):
        current = deck[i]
        walker = i - 1
        comparison += 1
        while walker >= 0 and cardInfo(deck[walker]) > cardInfo(current):
            deck[walker + 1] = deck[walker]
            walker -= 1
            comparison += 1
        deck[walker + 1] = current
        if walker < 0:
            comparison -= 1
        print(deck)
    print("Comparison times:", comparison)

def selectionSort(deck, last):
    comparison = 0
    for i in range(last):
        smallest = i
        for walker in range(i+1, last+1):
            if cardInfo(deck[walker]) < cardInfo(deck[smallest]):
                smallest = walker
            comparison += 1
        deck[i], deck[smallest] = deck[smallest], deck[i]
        print(deck)
    print("Comparison times:", comparison)

def bubbleSort(deck, last):
    comparison = 0
    for i in range(last):
        for walker in range(last-i):
            comparison += 1
            if cardInfo(deck[walker]) > cardInfo(deck[walker + 1]):
                deck[walker], deck[walker + 1] = deck[walker + 1], deck[walker]
        print(deck)
    print("Comparison times:", comparison)

def cardInfo(card):
    frontCard = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9, "J": 10, "Q": 11, "K": 12, "A": 13}
    patternCard = {"♣": 0, "♦": 1, "♥": 2, "♠": 3}#♣ < ♦ < ♥ < ♠
    return (frontCard[card[:-1]], patternCard[card[-1]])#'4♣'[-1]=♣, '4♣'[:-1]=4
insertionSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)
#selectionSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)
#bubbleSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)
