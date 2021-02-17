class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = Node()

    def insertIter(self,n):
        newnode = Node()
        newnode.data = n
        if(self.root.data ==  None):
            self.root = newnode
        else:
            temp = Node()
            temp = self.root
            while(1):
                if(n <= temp.data ):
                    if(temp.left == None):
                        temp.left = newnode
                        break
                    else:
                        temp = temp.left
                else:
                    if(temp.right == None):
                        temp.right = newnode
                        break
                    else:
                        temp = temp.right

    def insertRecur(self,node,n):
        if(node.data == None):
            node.data = n
            return
        if(n <= node.data):
            if(node.left == None):
                newnode = Node()
                newnode.data = n
                node.left = newnode
                return 
            else:
                self.insertRecur(node.left,n)
        else:
            if(node.right == None):
                newnode = Node()
                newnode.data = n
                node.right = newnode
                return 
            else:
                self.insertRecur(node.right,n)


    def traverseRecur(self,node):
        if(node.left):
            self.traverseRecur(node.left)    
        print(node.data,end=' ')
        if(node.right):
            self.traverseRecur(node.right)
      


bt = BinaryTree()
bt.insertIter(20)
bt.insertIter(22)
bt.insertIter(85)
bt.insertIter(19)
bt.insertIter(51)
bt.insertIter(0)
bt.insertIter(92)
bt.insertIter(64)
bt.insertIter(15)
bt.insertIter(5)
bt.insertRecur(bt.root,10)
bt.insertRecur(bt.root,12)
bt.insertRecur(bt.root,8)
bt.insertRecur(bt.root,15)
bt.insertRecur(bt.root,5)
bt.insertRecur(bt.root,10)
bt.insertRecur(bt.root,12)
bt.insertRecur(bt.root,8)
bt.insertRecur(bt.root,15)
bt.insertRecur(bt.root,5)
bt.traverseRecur(bt.root)

            
