"""Lab7.1 by Chirakit Marachchalee"""

from time import time

def summation1(n):
    total = 0
    for i in range(1,n+1):
        total += i
        #print(i) -> uncomment this if you want to know what happen inside this loop
    return total

def summation2(n):
    return (n * (n + 1)) / 2

def analyze_algo1(n=1):
    stime = time() #record the starting time
    summation1(n)
    etime = time() #record the ending time
    elapsed = etime - stime #computer the elapsed time
    print("execution time1:", elapsed)

def analyze_algo2(n=1):
    stime = time() #record the starting time
    summation2(n)
    etime = time() #record the ending time
    elapsed = etime - stime #computer the elapsed time
    print("execution time2:", elapsed)

analyze_algo1(10000)
analyze_algo2(10000)

#First summation1 is O(n)
#100            = ~0.0 sec
#10,000         = ~0.003999948501586914 sec 
#1,000,000      = ~0.07176017761230469 sec
#100,000,000    = ~4.03001070022583 sec
#1,000,000,000  = ~38.88441228866577 sec

#Second summation2 is O(1)
#100            = ~0.0 sec
#10,000         = ~0.0 sec 
#1,000,000      = ~0.0 sec
#100,000,000    = ~0.0 sec
#1,000,000,000  = ~0.0 sec
