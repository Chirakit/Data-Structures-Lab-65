"""Lab5 by Chirakit Marachchalee"""

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        if self.root == None:
            return True
        else:
            return False

    def insert(self, data) :
        pNew = BSTNode(data)
        prev = None
        start = self.root
        if self.is_empty():
            self.root = pNew
        else:
            while start != None:
                if data < start.data:
                    prev = start
                    start = start.left
                else:
                    prev = start
                    start = start.right
            #เชื่อมโหนด pNew
            if prev.right == start:
                prev.right = pNew
            else:
                prev.left = pNew

    def delete(self, data) :
        """delete data from BST"""
        start = self.root
        prev = None
        if self.is_empty():
            print("This is an empty tree!!")
            return False
        else:
            while data != start.data and data != None:
                if data < start.data:
                    prev = start
                    start = start.left
                else:
                    prev = start
                    start = start.right
            if start.left == None and start.right == None:
                if prev.data > data:
                    prev.left = None
                else:
                    prev.right = None
            elif start.left != None and start.right != None:
                checkp = start.left
                prev = start
                while checkp.right != None:
                    prev = checkp
                    checkp = checkp.right
                start.data = checkp.data
                prev.right = None
            elif start.left != None:
                checkp = start
                prev = start
                while checkp.left != None:
                    prev = checkp
                    checkp = checkp.left
                start.data = checkp.data
                prev.left = None
            else:
                if prev.data > data:
                    prev.left = start.right
                else:
                    prev.right = start.right

    def preorder(self, root) :
        if root != None:
            print("->", root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root) :
        if root != None:
            self.inorder(root.left)
            print("->", root.data, end=" ")
            self.inorder(root.right)

    def postorder(self, root) :
        if root != None:
            self.postorder(root.left)
            self.postorder(root.right)
            print("->", root.data, end=" ")

    def traverse(self) :
        if self.is_empty():
            print("This is an empty tree!!")
        else:
            print("\nPreorder: ")
            self.preorder(self.root)
            print("\nInorder: ")
            self.inorder(self.root)
            print("\nPostorder: ")
            self.postorder(self.root)

    def findMin(self) :
        """return minimum value"""
        start = self.root
        if self.is_empty():
            return None
        else:
            while start.left != None:
                start = start.left
        return start.data

    def findMax(self) :
        """return maximum value"""
        start = self.root
        if self.is_empty():
            return None
        else:
            while start.right != None:
                start = start.right
        return start.data


myBST = BST()
myBST.insert(14)
myBST.insert(23)
myBST.insert(7)
myBST.insert(10)
myBST.insert(33)
myBST.insert(5)
myBST.insert(13)
myBST.insert(20)
myBST.traverse()
print("-------")
myBST.delete(5)
myBST.traverse()
myBST.delete(33)
myBST.traverse()
myBST.delete(14)
myBST.traverse()
myBST.delete(7)
myBST.traverse()
myBST.delete(23)
myBST.traverse()
myBST.delete(13)
myBST.traverse()
