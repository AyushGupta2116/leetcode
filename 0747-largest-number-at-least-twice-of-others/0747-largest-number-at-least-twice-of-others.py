class Solution(object):
    def dominantIndex(self, nums):
        

        maxval = nums[0]

        for i in nums:
            if i > maxval:
                 maxval = i


        index = nums.index(maxval)

        for i in range(0,len(nums)):
            if i != index:
                if maxval < 2 * nums[i]:
                    return -1

        return index
        