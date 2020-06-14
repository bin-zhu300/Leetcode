class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arr2= [item for items, c in Counter(arr).most_common() for item in [items] * c]        
        while k>0:
            arr2.pop()
            k-=1
        return len(set(arr2))
    
# https://docs.python.org/2/library/collections.html
# https://www.geeksforgeeks.org/python-sort-list-elements-by-frequency/
# https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/