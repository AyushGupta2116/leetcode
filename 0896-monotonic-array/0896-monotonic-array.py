class Solution(object):
    def isMonotonic(self, nums):

        if nums == sorted(nums):
            return True

        if nums == sorted(nums, reverse=True):
            return True

        return False