class Solution(object):
    def moveZeroes(self, nums):
        temp = []
        l = len(nums)

        for i in range(l):
            if nums[i] != 0:
                temp.append(nums[i])

        m = len(temp)

        for i in range(m):
            nums[i] = temp[i]

        for i in range(m, l):
            nums[i] = 0