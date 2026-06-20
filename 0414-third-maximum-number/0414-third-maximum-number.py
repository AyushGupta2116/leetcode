class Solution(object):
    def thirdMax(self, nums):
        nums.sort(reverse=True)

        count = 1
        current = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != current:
                count += 1
                current= nums[i]

            if count == 3:
                return nums[i]

        return nums[0]