class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        ans = sorted(nums1+nums2)
        l= len(ans)
        mid = int(l/2)
        
        if(l%2==0):
            return float(ans[mid-1] + ans[mid])/2
        else:
            return ans[mid]
        