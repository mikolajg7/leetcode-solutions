class Solution(object):
    def productExceptSelf(self, nums):
        answ = []
        for i, n in enumerate(nums):
            result = reduce(lambda x, y: x * y, nums[:i] + nums[i + 1:])
            answ.append(result)
        return answ
