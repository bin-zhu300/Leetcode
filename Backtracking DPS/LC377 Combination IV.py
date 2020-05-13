#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:56:44 2020

@author: Bin
"""

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res=[]
        def dfs(idx,temp,Target):
            if Target==0:
                res.append(temp[:])
            for i in range(idx,len(nums)):
                if nums[i]>Target:
                    continue
                temp.append(nums[i])
                dfs(idx,temp,Target-nums[i])
                temp.pop()
        
        dfs(0,[],target)
        
        res_cnt=len(res)

        return res_cnt
    
    #ETL, DP