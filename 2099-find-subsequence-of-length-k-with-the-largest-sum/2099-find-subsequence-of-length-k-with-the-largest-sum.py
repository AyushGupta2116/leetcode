class Solution(object):
    def maxSubsequence(self, nums, k):
        arr = []

        for i in range(len(nums)):
            arr.append([nums[i], i])

        arr.sort(reverse=True)
        arr = arr[:k]

        arr.sort(key=lambda x: x[1])

        ans = []
        for i in arr:
            ans.append(i[0])

        return ans 
        
            
            

        