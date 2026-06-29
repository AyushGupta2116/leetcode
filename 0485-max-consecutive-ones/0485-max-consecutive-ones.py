class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count =0
        maxe = 0
        for i in range (0,len(nums)):
            if nums[i]==1:
                count = count +1
                maxe = max(maxe,count)
            else:
                count =0
        
        return maxe

        