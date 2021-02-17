class Node:

    def __init__(self):
        self.data = 0
        self.next = None

        

class LinkedList:

    def __init__(self):
        self.head = None

    def insertBeg(self,i):
        newnode = Node()
        newnode.data = i
        if(self.head == None):
            self.head = newnode
        else:
            newnode.next = self.head      
            self.head = newnode

    def insertEnd(self,i):
        newnode = Node()
        newnode.data = i
        if(self.head == None):
            self.head = newnode
        else:
            temp = Node()
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = newnode

    def traverse(self):
        tempnode = Node()
        tempnode = self.head
        while(tempnode):
            print(tempnode.data,end=' ')
            tempnode = tempnode.next
        print()   

    def deleteBeg(self):
        self.head = self.head.next
        if(self.countNodes() ==0):
            return

    def deleteEnd(self):
        if(self.countNodes() ==0):
            return
        if(self.countNodes() == 1):
            self.deleteBeg()
            return
        temp = Node()
        temp = self.head
        while ((temp.next).next) :
            temp = temp.next
        temp.next = None  

    def countNodes(self):
        temp = Node()
        temp = self.head
        count = 0
        while (temp):
            count = count +1
            temp = temp.next
        return count      

    def front(self):
        return self.head.data

    def end(self):
        temp = Node()
        temp = self.head
        while(temp.next):
            temp = temp.next
        return temp.data

    def reverse(self):
        nl = LinkedList()
        while(self.head):
            nl.insertBeg(self.front())
            self.deleteBeg()
        return nl        


