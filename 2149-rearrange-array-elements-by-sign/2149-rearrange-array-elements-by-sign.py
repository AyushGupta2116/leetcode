class Solution(object):
    def rearrangeArray(self, nums):
        n  = len(nums)
        pindex =0
        nindex =1
        ans = [0] * n
        
        for i in nums:
            if i<0:
               ans[nindex] = i
               nindex = nindex+2
            else:
                ans[pindex]= i
                pindex = pindex+2

        return ans