class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen=set() # set of seen letters
        for n in nums:
            if n in seen:
                return True # if anny value appears at least twice, return true
            seen.add(n)
        return False # otherwise return false