class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)
        mx = nums[0]
        mn = [0] * n
        mn[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            mn[i] = min(mn[i + 1], nums[i])

        for i in range(n):
            mx = max(mx, nums[i])
            if mx - mn[i] <= k:
                return i

        return -1