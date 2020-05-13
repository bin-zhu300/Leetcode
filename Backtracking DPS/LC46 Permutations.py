#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:56:44 2020

@author: Bin
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(idx,temp,used):         #关键：加入这个used
            if len(temp)==len(nums):
                res.append(temp[:])
            for i in range(idx,len(nums)):
                if nums[i] in used:
                    continue
                used.append(nums[i])    #关键：加入这个used
                temp.append(nums[i])
                dfs(idx,temp,used)      #关键：从idx（头）开始
                temp.pop()
                used.pop()              #关键：加入这个used.pop()
                
        dfs(0,[],[])
        
        return res