#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 22:53:24 2020

@author: Bin
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def dfs(idx=0,temp=[]):
            if temp not in res:
                res.append(temp[:])
            for i in range(idx,len(nums)):
                temp.append(nums[i])
                dfs(i+1,temp)
                temp.pop()
        
        dfs()
        
        return res