#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:56:43 2020

@author: Bin
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def dfs(idx,temp,target,k):
            if target==0 and k==0:      #注意这里是k==0
                res.append(temp[:])
            for i in range(idx,10):
                temp.append(i)
                dfs(i+1,temp,target-i,k-1)
                temp.pop()
            
        dfs(1,[],n,k)
        
        return res
                