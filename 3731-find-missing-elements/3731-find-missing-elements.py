class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()
        s = set(nums)
        missing = []

        for i in range(nums[0], nums[-1]):
            if i not in s:
                missing.append(i)

        return missing