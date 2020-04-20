# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:08:48 2020

@author: NK
"""

#Stacks implementation using array: LIFO

class Stack:
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return self.stack == []
    
    def push(self, data):
        self.stack.append(data)
        
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
#Testing
st = Stack()
st.push(1)
st.push(2)
st.push(3)
st.push(5)
st.pop()
st.size()
st.push(6)
st.pop()
st.peek()