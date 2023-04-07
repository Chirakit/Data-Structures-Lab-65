"""Lab8 by Chirakit Marachchalee"""

class ProbHash:
    def __init__(self, cap):
        self.hashtable = cap * [None] #This is list.
        self.n = cap #ขนาด Hashtable

    def hashFunction(self, mykey):
        hashkey = mykey % self.n
        return hashkey

    def rehashFuntion(self, hashkey):
        rehash = (hashkey + 1) % self.n
        return rehash

    def insertData(self, student_obj):
        id_stu = student_obj.getId()
        key = self.hashFunction(id_stu)
        if self.hashtable[key] == None:
            self.hashtable[key] = student_obj
            print("insert %s at index %d"%(id_stu, key))
            return
        else:
            count = 0
            while (self.hashtable[key] != None) and (count <= self.n):
                key = self.rehashFuntion(key)
                count += 1
            if count <= self.n:
                self.hashtable[key] = student_obj
                print("insert %s at index %d"%(id_stu, key))
            else:
                print("HarshTable is Full!!!")

    def searchData(self, key):
        index = self.hashFunction(key)
        if self.hashtable[index] != None:
            if self.hashtable[index].id == key:
                print("Found %s at index %d"%(key, index))
                return self.hashtable[index]
            else:
                count = 0
                while self.hashtable[index] != None and count <= self.n:
                    index = self.rehashFuntion(index)
                    if self.hashtable[index] is None:
                        print("%s does not exist."%key)
                        return
                    elif self.hashtable[index].id == key:
                        print("Found %s at index %d"%(key, index))
                        return self.hashtable[index]
                    count += 1
        print("%s does not exist."%key)


class Student:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getGpa(self):
        return self.gpa

    def printDetails(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("GPA:", self.gpa)

s1 = Student(65070001, "Sandee Boonmak", 3.05)
s2 = Student(65070077, "Somsak Jaidee", 2.78)
s3 = Student(65070021, "Somsri Jaiyai", 3.44)
s4 = Student(65070042, "Sommai Meeboon", 2.89)
myHash = ProbHash(20)
myHash.insertData(s1)
myHash.insertData(s2)
myHash.insertData(s3)
myHash.insertData(s4)
print("")
std = myHash.searchData(65070077)
std.printDetails()
print("-------------------------")
std = myHash.searchData(65070021)
std.printDetails()
print("-------------------------")
std = myHash.searchData(65070042)
std.printDetails()
print("-------------------------")
std = myHash.searchData(65070032)
