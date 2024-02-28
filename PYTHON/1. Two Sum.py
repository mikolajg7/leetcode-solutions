class Solution(object):
    def twoSum(self, nums, target):
     seen={} #dictionary help us with the problem of adding the same number
     for index, value in enumerate(nums):
         newtarget=target-value
         if newtarget in seen: # if we saw this number earlier, we return earlier number anc current one
             return seen[newtarget],index
         seen[value]=index #otherwise add this number to dictionary