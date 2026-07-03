class Solution(object):
    def merge(self, nums):
        n = len(nums)
        nums.sort()

        ans = []
        last = -1

        for i in range(n):

            if i <= last:
                continue

            start = nums[i][0]
            end = nums[i][1]

            for j in range(i + 1, n):

                if nums[j][0] <= end:
                    end = max(end, nums[j][1])
                    last = j
                else:
                    break

            ans.append([start, end])

        return ans