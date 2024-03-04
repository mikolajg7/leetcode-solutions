class Solution:
    # basically the same soulution as in 1. two sums just checking which index is lower
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        ans={}
        for index, value in enumerate(numbers):
            newtarget=target-value
            if newtarget in ans:
                return [min(ans[newtarget],index)+1,max(ans[newtarget],index)+1]
            ans[value]=index

