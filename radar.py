# -*- coding: utf-8 -*-
"""
Created on Tue May 23 12:23:11 2017

@author: AlphaTao
#radar installation
"""
import numpy
def solve():
    
    ans=1
    now=s[0].right
    for i in range(n):
        if s[i].left<=now:
            now = min(now, s[i].right)
        else:
            ans+=1
            now = s[i].right
    return ans

class node:
    def __init__(self,d,x,y):
        self.left=x-numpy.sqrt(d*d-y*y)
        self.right=x+numpy.sqrt(d*d-y*y)

if __name__=="__main__":
    n,d = map(int,raw_input().split())
    s=[]
    for i in range(n):
        x,y=map(int,raw_input().split())
        s.append(node(d,x,y))
    s.sort(key=lambda node: node.left)
    print solve()