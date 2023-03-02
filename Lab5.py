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

            prev.right = pNew


    def delete(self, data) :
        #// delete data from BST
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
        #// return minimum value
        return
    def findMax(self) :
        #// return maximum value
        return


myBST = BST()
myBST.insert(10)
myBST.insert(15)
myBST.insert(25)
myBST.insert(35)
myBST.traverse()
