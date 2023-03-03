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
            if (prev.right == start):
                prev.right = pNew
            else:
                prev.left = pNew

    def delete(self, data) :
        """delete data from BST"""
        return

    def preorder(self, root) :
        if (root != None):
            print("->", root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root) :
        if (root != None):
            self.inorder(root.left)
            print("->", root.data, end=" ")
            self.inorder(root.right)

    def postorder(self, root) :
        if (root != None):
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
myBST.traverse()
print("Min:", myBST.findMin())
print("Max:", myBST.findMax())
