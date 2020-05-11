#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 12:04:33 2020

@author: Bin
"""

from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        d=defaultdict(list)
        for u,v in edges:
            d[u].append(v)
        
        def dfs(node): #从这个node开始，搜集完所有苹果所需时间
            cnt=0
            for child in d[node]:
                cost=dfs(child)  #必须放在这里，不然超时
                if cost>0 or hasApple[child]: #这里的cost不能用dfs(child),不然超时
                    cnt+=cost+2
            return cnt
        
        return dfs(0)
    
    
#参考： https://zxi.mytechroad.com/blog/    


            
        
    
    
    
    
    
    


