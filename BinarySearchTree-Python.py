# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 00:18:57 2020

@author: NK
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        newNode = Node(data)
        if not self.root:
            self.root = newNode
        else:
            currNode = self.root
            prevNode = self.root
            while currNode is not None:
                prevNode = currNode
                if currNode.data > data:
                    currNode = currNode.leftChild
                else:                    
                    currNode = currNode.rightChild
            if prevNode.data > data:
                prevNode.leftChild = newNode
            else:
                prevNode.rightChild = newNode
    
    def insertRecursive(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(self.root, data)
            
    def insertNode(self, node, data):
        if node.data > data:
            if node.leftChild:
                self.insertNode(node.leftChild, data)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(node.rightChild, data)
            else:
                node.rightChild = Node(data)
            
    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):
        if node.leftChild:
            return self.getMin(node.leftChild)
        return node.data                
    
    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)
        
    def getMax(self, node):
        if node.rightChild:
            return self.getMax(node.rightChild)
        return node.data
    
    def traverse(self):
        if self.root:
            self.traverseInorder(self.root)
            
    def traverseInorder(self, node):
        if node.leftChild:
            self.traverseInorder(node.leftChild)
        print("%s " % node.data)
        if node.rightChild:
            self.traverseInorder(node.rightChild)
    
    def remove(self, data):
        if self.root:
            self.root = self.removeNode(self.root, data)
    
    def removeNode(self, node, data):
        if not node:
            return node
        if node.data > data:
            node.leftChild = self.removeNode(node.leftChild, data)
        elif node.data < data:
            node.rightChild = self.removeNode(node.rightChild, data)
        else:
            if not node.leftChild and not node.rightChild:
                print("removing a leaf node..")
                del node
                return None
            if not node.leftChild:
                print("removing a node with only right child")
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print("removing a node with only left child")
                tempNode = node.leftChild
                del node
                return tempNode
            
            print("Removing node with two children..")
            #Swap with largest value in left subtree
            tempNode = self.getMaxNode(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(node.leftChild, tempNode.data)
        
        return node
        
    def getMaxNode(self, node):
        if node.rightChild:
            return self.getMaxNode(node.rightChild)
        return node
        
    
##Testing
bst = BinarySearchTree()
bst.insertRecursive(2)
bst.insertRecursive(3)
bst.insertRecursive(1)
bst.insertRecursive(5)
bst.insertRecursive(0)
bst.insertRecursive(4)
bst.insertRecursive(9)
bst.insertRecursive(-2)

bst.traverse()
bst.getMaxValue()
bst.getMinValue()
    
bst = BinarySearchTree()
bst.insertRecursive("A")
bst.insertRecursive("D")
bst.insertRecursive("B")
bst.insertRecursive("C")
    
bst.getMaxValue()
bst.traverse()    
    
#Testing deletion
bst = BinarySearchTree()
bst.insertRecursive(2)
bst.insertRecursive(3)
bst.insertRecursive(1)
bst.insertRecursive(5)
bst.insertRecursive(0)

bst.getMaxNode(bst.root).data

bst.remove(3)
bst.traverse()



