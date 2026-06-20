class Solution(object):
    def thirdMax(self, nums):
        new_nums = list(set(nums))
        new_nums.sort(reverse=True)

        if len(new_nums) >= 3:
            return new_nums[2]
        return new_nums[0]