#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 18:31:13 2020

@author: Bin
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if not intervals:
            return []
        else:
            new=[intervals[0]]
            for e in intervals:
                if e[0]<=new[-1][1]:
                    new[-1][1]=max(new[-1][1],e[1])
                else:
                    new. append(e)
            return new
