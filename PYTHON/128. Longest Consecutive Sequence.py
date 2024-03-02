class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums=set(nums)
        longest=0
        for n in nums:
            if n-1 not in nums:
                curr_n =n
                curr_sreak=1
                while curr_n+1 in nums:
                    curr_n+=1
                    curr_sreak+=1
                longest=max(curr_sreak,longest)
        return longest


