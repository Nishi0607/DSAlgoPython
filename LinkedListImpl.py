# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:52:07 2020

@author: NK
"""

class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.nextNode = None
    
class LinkedList(object):

    def __init__(self):
        self.head=None
        self.size=0
        
    def insertAtStart(self, data):
        self.size = self.size+1
        newNode = Node(data)
        
        if not self.head:
            self.head=newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
            
    # O(1)
    def size(self):
        return self.size

    # O(N)
    def size2(self):
        currNode = self.head
        size = 0
        while currNode is not None:
            size += 1
            currNode = currNode.nextNode
        
        return size
    
    def insertAtEnd(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            currNode = self.head
            while currNode.nextNode is not None:
                currNode = currNode.nextNode
                
            currNode.nextNode = newNode
        self.size += 1
                
    def traverseList(self):
        currNode = self.head
        while currNode is not None:
            print("%d " % currNode.data)
            currNode = currNode.nextNode
            
    def remove(self, data):
        if not self.head:
            return;
        currNode = self.head
        prevNode = None
        
        while currNode.data!=data:
            prevNode = currNode
            currNode = currNode.nextNode            
            if currNode is None:
                break
        
        if(currNode==self.head):
            self.head = currNode.nextNode
        elif currNode is None:
            return;
        else:
            prevNode.nextNode = currNode.nextNode
            currNode = None
            

#Testing
myList = LinkedList()

myList.insertAtStart(2)
myList.insertAtStart(3)
myList.insertAtStart(5)
myList.insertAtStart(6)
myList.remove(6)

print(myList.head.data)

myList.traverseList()
        
        