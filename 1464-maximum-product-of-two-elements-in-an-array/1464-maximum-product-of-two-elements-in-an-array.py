class Solution(object):
    def maxProduct(self, nums):
        l = len(nums)
        nums = sorted(nums)
        return (nums[l-1]-1) * (nums[l-2]-1)
        