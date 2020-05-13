#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:56:43 2020

@author: Bin
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(idx=0,temp=[],T=target):
            if T==0:
                res.append(temp[:])
            for i in range(idx,len(candidates)):
                if candidates[i]>T:
                    continue
                temp.append(candidates[i])
                dfs(i,temp,T-candidates[i])  #特别注意： T-candidtes[i] 不是 T-sum(Temp)
                temp.pop()
        
        dfs()
        
        return res
        