
class Solution(object):
    def minMoves2(self, nums):
        nums.sort()

        mid = len(nums) // 2
        median = nums[mid]

        count = 0

        for i in nums:
            count += abs(i - median)

        return count

        