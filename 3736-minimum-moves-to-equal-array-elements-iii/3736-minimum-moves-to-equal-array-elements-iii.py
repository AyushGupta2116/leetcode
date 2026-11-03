class Solution(object):
    def minMoves(self, nums):
        maxi = max(nums)
        count = 0

        for i in nums:
            count += maxi - i

        return count