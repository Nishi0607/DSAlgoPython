# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 22:14:43 2020

@author: NK
"""

#Queue implementation in Python
class Queue:
    def __init__(self):
        self.queue = []
        
    def isEmpty(self):
        self.queue == []
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        if len(self.queue)==0 :
            return -1
        data = self.queue[0]
        del self.queue[0]
        return data
    
    def peek(self):
        return self.queue[0] if len(self.queue)>0 else -1
    
    def size(self):
        return len(self.queue)
    
    
#Testing
q = Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print("Size %d" % q.size())

q.dequeue()
print("Peek queue: %d" % q.peek())  

q.dequeue()
print("Size %d" % q.size())
print("Peek queue: %d" % q.peek())  


q.dequeue()
print("Size %d" % q.size())
print("Peek queue: %d" % q.peek())  