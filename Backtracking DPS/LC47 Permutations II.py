#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:56:44 2020

@author: Bin
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(idx,temp,used):         
            if len(temp)==len(nums) and temp not in res:
                res.append(temp[:])                   
            for i in range(idx,len(nums)):
                if i in used:
                    continue
                used.append(i)          #关键：把nums[i]换成i 即可
                temp.append(nums[i])
                dfs(idx,temp,used)      
                temp.pop()
                used.pop()              
                
        dfs(0,[],[])
        
        return res