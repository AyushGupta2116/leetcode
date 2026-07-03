class Solution:
    def fourSum(self, arr, target):
        n = len(arr)

        ans = set()
        result = []

        for i in range(n):

            for j in range(i + 1, n):

                hashset = set()

                for k in range(j + 1, n):

                    fourth = target - (arr[i] + arr[j] + arr[k])

                    if fourth in hashset:
                        quad = tuple(sorted([arr[i], arr[j], arr[k], fourth]))
                        ans.add(quad)

                    hashset.add(arr[k])

        for x in ans:
            result.append(list(x))

        return result