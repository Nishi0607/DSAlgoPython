# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:59:41 2020

@author: NK
"""

class CircularNode(object):
    
    def __init__(self, data):
        self.nextNode = None
        self.data = data
        

class CircularList(object):
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insertAtEnd(self, data):
        newNode = CircularNode(data)
        self.size+=1
        if self.head is None:
            self.head = newNode
            self.head.nextNode = self.head
        else:
            currNode = self.head
            while currNode.nextNode!=self.head:
                currNode = currNode.nextNode
            
            currNode.nextNode = newNode
            newNode.nextNode = self.head
            
    def delete(self, data):
        if self.head is None:
            return
        else:
            currNode = self.head
            prevNode = self.head
            while currNode.data!=data:
                prevNode = currNode
                currNode = currNode.nextNode
                if currNode.nextNode==self.head:
                    break
            #If the node to delete is found to be head itself
            if currNode==self.head and currNode.data==data:
                #If head is the only node in the circular linked list
                if currNode.nextNode==self.head:
                    currNode = None
                    self.head.nextNode = None
                    self.head = None
                #If there are nodes other than head in the list
                else:
                    iter = currNode
                    while iter.nextNode!=self.head:
                        iter = iter.nextNode
                    iter.nextNode = self.head.nextNode
                    self.head = iter.nextNode
                    currNode = None
                    
            #Else if we found the node (intermediate node, other than head)
            elif currNode.data==data:
                prevNode.nextNode = currNode.nextNode
                currNode = None
                self.size-=1
            #Else, we did not find the node
            else:
                return
                
    def size2(self):
        if self.head is None:
            return 0
        else:
            size = 0
            currNode = self.head
            while(currNode.nextNode!=self.head):
                currNode = currNode.nextNode
                size+=1
            
            return size
     
    def traverseList(self):
        if self.head is None:
            return
        else:
            currNode = self.head
            print("Head %d " % currNode.data)
            while currNode.nextNode != self.head:
                currNode = currNode.nextNode
                print("Node %d " % currNode.data)

#Testing the CircularList

clist = CircularList()
clist.insertAtEnd(2)            
clist.insertAtEnd(3)
clist.insertAtEnd(4)
clist.insertAtEnd(5)
clist.insertAtEnd(6)
clist.delete(3)
clist.delete(2)
clist.delete(4)
clist.delete(5)
clist.delete(6)


clist.traverseList()