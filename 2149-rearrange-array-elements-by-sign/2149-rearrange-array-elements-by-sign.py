class Solution(object):
    def rearrangeArray(self, nums):
        pindex =0
        nindex =1
        ans = [0] * len(nums)
        
        for i in range(0,len(nums)):
            if nums[i]<0:
               ans[nindex] = nums[i]
               nindex = nindex+2
            else:
                ans[pindex]= nums[i]
                pindex = pindex+2

        return ans