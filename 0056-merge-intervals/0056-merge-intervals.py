class Solution(object):
    def merge(self, arr):

        arr.sort()

        ans = []

        for i in range(len(arr)):

            start = arr[i][0]
            end = arr[i][1]

            if len(ans) == 0:
                ans.append([start, end])

            else:

                if start <= ans[-1][1]:
                    ans[-1][1] = max(ans[-1][1], end)

                else:
                    ans.append([start, end])

        return ans