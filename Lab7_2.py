"""Lab7.2 by Chirakit Marachchalee"""

from time import time
from random import randint
def isIntersect1(a, b, c):
    empt = []
    for i in a:
        for j in b:
            if i == j:
                empt.append(i)
    for k in c:
        if k in empt:
            return True
    return False

def isIntersect2(a, b, c):
    for i in a:
        for j in b:
            for k in c:
                if i == j == k:
                    return True
    return False

def randomList(n):
    return [randint(0,1000000) for _ in range(n)]

def analyze_algo1(n=1):
    a = randomList(n)
    b = randomList(n)
    c = randomList(n)
    stime = time() #record the starting time
    isIntersect1(a, b, c)
    etime = time() #record the ending time
    elapsed = etime - stime #computer the elapsed time
    print("execution time1:", elapsed)

def analyze_algo2(n=1):
    a = randomList(n)
    b = randomList(n)
    c = randomList(n)
    stime = time() #record the starting time
    isIntersect2(a, b, c)
    etime = time() #record the ending time
    elapsed = etime - stime #computer the elapsed time
    print("execution time1:", elapsed)

#print(isIntersect1([50, 20, 80], [40, 30, 20], [20, 70, 90])) -> True
#print(isIntersect1([40, 60, 80, 100], [10, 30, 50, 60], [10, 20, 30, 40])) -> False
#print(isIntersect1(randomList(3), randomList(3), randomList(3))) -> Depend on your luck result True or False

analyze_algo2(100)

#isIntersect1
#100    = ~0.0 sec
#1000   = ~0.017000675201416016 sec
#10000  = ~1.8709957599639893 sec
#100000 = ~180 sec result ~156.1069893836975 sec

#isIntersect2
#100    = ~0.018999576568603516 sec
#1000   = ~20.17415475845337 sec
#10000  = ~20000 sec
#100000 = ~20000000 sec
