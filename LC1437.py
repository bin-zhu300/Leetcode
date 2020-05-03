#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 00:05:18 2020

@author: Bin
"""

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        cnt=0
        l=len(nums)
        track=[]
        for i in nums:
            if i==1:
                track.append(cnt)
                cnt=0
            else:
                cnt+=1
        track.append(cnt)
                
        track=list(filter((0).__ne__,track))
        if k==0 and not track:
            return True
        elif not track and k>0:
            return False
        elif min(track)<k:
            return False
        else:
            return True
                