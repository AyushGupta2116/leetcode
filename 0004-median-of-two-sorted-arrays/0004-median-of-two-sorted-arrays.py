class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        m = len(nums1)
        n = len(nums2)

        ans = []
        i = 0
        j = 0

        while i < m and j < n:

            if nums1[i] < nums2[j]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1

        while i < m:
            ans.append(nums1[i])
            i += 1

        while j < n:
            ans.append(nums2[j])
            j += 1

        l = len(ans)

        if l % 2 != 0:
            mid = l /2
            return float(ans[mid])

        else:
            mid = l / 2
            return (ans[mid] + ans[mid - 1]) / 2.0