class Solution(object):
    def twoSum(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in h:
                return h[diff], i
            h[num] = i
