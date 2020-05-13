#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:56:45 2020

@author: Bin
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        res=[]
        def dfs(idx,temp):
            if len(temp)==len(digits):
                res.append(''.join(temp[:]))
                return                          #这里这个return 必须在，不然会超出界限
                #其他题目不用，因为 idx会带入到下一个for loop，当idx>=len(nums) 时，自动退出了
            for e in phone[digits[idx]]:
                temp.append(e)
                dfs(idx+1,temp)
                temp.pop()
        
        if not digits:
            return []
        else:
            dfs(0,[])
            return res