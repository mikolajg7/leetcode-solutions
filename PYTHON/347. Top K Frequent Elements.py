from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        answ=[]
        sort=Counter(nums)  # returns dictionary of numbers with their quantity
        sorted_nums=sorted(sort, key=lambda x: sort[x], reverse=True)  # sorting by frequency  
        return list(sorted_nums)[:k]
