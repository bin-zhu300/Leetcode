#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:56:43 2020

@author: Bin
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(idx=0,temp=[],T=target):
            if T==0:
                a=sorted(temp[:])             #此处必须是shallow copy
                if a not in res:
                    res.append(a)
            for i in range(idx,len(candidates)):
                if candidates[i]>T:
                    continue
                temp.append(candidates[i])
                dfs(i+1,temp,T-candidates[i])
                temp.pop()

        dfs()
        
        return res
        