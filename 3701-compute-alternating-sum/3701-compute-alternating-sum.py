class Solution(object):
    def alternatingSum(self, nums):
        sum0 =0
        sum1=0
        for i in range (0,len(nums),2):
            sum0 = sum0+nums[i]
        for j in range (1,len(nums),2):
            sum1 = sum1+nums[j]
        
        return sum0-sum1
        