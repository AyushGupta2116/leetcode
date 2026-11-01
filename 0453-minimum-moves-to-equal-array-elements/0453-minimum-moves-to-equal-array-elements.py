
class Solution(object):
    def minMoves(self, nums):
        mini = min(nums)
        count = 0

        for i in nums:
            count += i - mini

        return count

        