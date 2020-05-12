#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 22:53:21 2020

@author: Bin
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(idx=0,temp=[]):
            # if len(temp)<=len(nums):   # 这个条件不需要也可以，因为range(4,3)无效
            res.append(temp[:])          #此处必须shallow copy
            for i in range(idx,len(nums)):
                temp.append(nums[i])     # 1. 存入result
                dfs(i+1,temp)            # 2. Recursion
                temp.pop()               # 3. 开始下一个循环前移除nums[i]
                
            
        dfs()    
        
        return res
    
    # Ref: https://www.youtube.com/watch?v=rtFHxiQAICA
    #      https://www.youtube.com/watch?v=CUzm-buvH_8&t=128s

                
  