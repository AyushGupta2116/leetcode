class Solution(object):
    def dominantIndex(self, nums):
        maxval = max(nums)
        index = nums.index(maxval)

        for i in range(0,len(nums)):
            if i != index:
                if maxval < 2 * nums[i]:
                    return -1

        return index
        