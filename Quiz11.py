def quiz1(n):
    if(n == 1):
        r1 = 12
    else:
        r1 = n + quiz1(n/2)
    return r1

def quiz2(n):
    if(n == 8):
        print("Go Back!")
    else:
        print(str(n) + "Hello!")
        quiz2(n + 2)
        print(str(n) + "Bye!")

def quiz3(x):
    if(x < 5):
        return(3 * x)
    else:
        return(2 * quiz3(x - 5) + 7)

    print("Finish!!")
    return 1
