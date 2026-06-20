class Solution(object):
    def findNumbers(self, nums):
        count1 = 0

        for i in range(len(nums)):
            num = nums[i]     
            count = 0

            while num > 0:
                num = num // 10
                count += 1

            if count % 2 == 0:
                count1 += 1

        return count1
                
