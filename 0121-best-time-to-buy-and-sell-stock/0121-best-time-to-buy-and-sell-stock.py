class Solution(object):
    def maxProfit(self, nums):
        profit =0
        mini = nums[0]
        for i in range(0,len(nums)):
            cost  = nums[i]-mini
            profit = max(profit,cost)
            mini = min(mini,nums[i])
        return profit
        