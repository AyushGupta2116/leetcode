class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        result = []
        n = len(nums2)

        for j in nums1:
            found = False
            ans = -1

            for i in range(n):
                if nums2[i] == j:
                    found = True
                elif found and nums2[i] > j:
                    ans = nums2[i]
                    break

            result.append(ans)
            

        return result
            
                

        
        