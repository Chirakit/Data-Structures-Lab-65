"""Lab02 By Chirakit Marchchalee"""

class DataNode:
    def __init__(self, input_name=""):
        self.name = input_name
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def traverse(self):
        if self.head == None:#empty list
            print("This is an empty list.")
        else:
            pos = self.head
            while pos != None:
                print("->", pos.name, end=" ")
                pos = pos.next
            print("")
        return

    def insertFront(self, data):
        pNew = DataNode(data)
        if self.head == None:#empty list
            self.head = pNew
        else:
            pNew.next = self.head
            self.head = pNew
        self.count += 1
        return

    def insertLast(self, data):
        pNew = DataNode(data)
        if self.head == None:#empty list
            self.head = pNew
        else:
            pos = self.head
            while pos.next != None:
                pos = pos.next
            pos.next = pNew
        self.count += 1
        return

    def insertBefore(self, node, data):
        pNew = DataNode(data)
        pos = self.head
        while pos.next != None:
            if pos.next.name == node:
                pNew.next = pos.next
                pos.next = pNew
                return
            pos = pos.next
        print("Cannot insert, <node> does not exist.")

    def delete(self, data):
        if self.head == None:
            return print("Cannot delete " + data + " does not exist.")
        start = self.head
        prev = None
        while start.name != data:
            prev = start
            if start.next == None:
                return print("Cannot delete " + data + " does not exist.")
            start = start.next

        if prev == None:
            self.head = self.head.next
        elif start.next == None:
            prev.next = None
        else:
            prev.next = start.next
        del start



mylist = SinglyLinkedList()
mylist.insertLast("John")
mylist.insertLast("Tony")
mylist.insertFront("Bill")
mylist.traverse()
mylist.insertBefore("Tony", "Kim")
mylist.traverse()
mylist.delete("John")
mylist.traverse()
mylist.insertFront("Meg")
mylist.traverse()
