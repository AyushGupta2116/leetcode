class Solution(object):
    def rearrangeArray(self, nums):
        n  = len(nums)
        pindex =0
        nindex =1
        ans = [0] * n
        
        for i in range(n):
            if nums[i]<0:
               ans[nindex] = nums[i]
               nindex = nindex+2
            else:
                ans[pindex]= nums[i]
                pindex = pindex+2

        return ans