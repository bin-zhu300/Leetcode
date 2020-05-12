#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 22:53:24 2020

@author: Bin
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def dfs(idx=1,temp=[]):
            if len(temp)==k:
                res.append(temp[:])
            for i in range(idx,n+1):
                temp.append(i)
                dfs(i+1,temp)
                temp.pop()
        
        dfs()
        return res