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
        return id_stu

    def searchData(self, key):
        pass

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
        print("ID:", Student.getId())
        print("Name:", Student.getName())
        print("GPA:", Student.getGpa())

s1 = Student(65070001, "Sandee Boonmak", 3.05)
myHash = ProbHash(20)
myHash.insertData(s1)
