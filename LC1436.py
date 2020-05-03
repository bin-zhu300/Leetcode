#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 00:06:20 2020

@author: Bin
"""

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        a=dict(paths)
        start=paths[0][0]
        while start in a.keys():
            start=a[start]
        return start