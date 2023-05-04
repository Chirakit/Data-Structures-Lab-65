"""Lab10 by Chirakit Marachchalee"""

class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getWeight(self):
        return self.weight

    def getCost(self):
        return self.price / self.weight

def coinExchange(amount, coinList):
    coins = [10, 5, 2, 1]
    coinstype = [0, 0, 0, 0]
    result = 0
    newAmount = amount
    for i in range(len(coins)):
        while amount >= coins[i] and coinList[i] > 0:
            newAmount -= coins[i]
            coinList[i] -= 1
            coinstype[i] += 1
            result += 1
    if newAmount > 0:
        print("Coins are not enough.")
    else:
        print("Amount:", amount)
        print("Coin exchange result:", coinstype)
        print("Number of coins:", result)

def knapsack(amount, itemList):
    itemList.sort(key = lambda a: a.getCost(), reverse = True)
    result = []
    value = 0
    weight = amount
    for i in itemList:
        if i.getWeight() <= weight:
            result.append(i)
            value += i.getPrice()
            weight -= i.getWeight()
    print("Knapsack Size:", amount, "kg")
    print("=" * 30)
    for j in result:
        print(j.getName(), "->", j.getWeight(), "kg", j.getPrice(), "THB")
    print("Total:",value, "THB")

"""
#*** Coin Exchange ***
coinList = [10, 10, 10, 10]
coinExchange(127, coinList)
"""

"""
#*** KNAPSACK (1) ***
item1 = Item('stereo', 3000, 3)
item2 = Item('laptop', 2000, 2)
item3 = Item('guitar', 1500, 1.5)
itemList = [item1, item2, item3]
knapsack(3.5, itemList)
"""

"""
#*** KNAPSACK (2) ***
item1 = Item('tablet', 7000, 0.5)
item2 = Item('perfume', 6000, 0.5)
item3 = Item('guitar', 9000, 1)
item4 = Item('air purifier', 9000, 2)
item5= Item('watch', 8000, 0.5)
itemList = [item1, item2, item3, 
item4, item5]
knapsack(3, itemList)
"""
