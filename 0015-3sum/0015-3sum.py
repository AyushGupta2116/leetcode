class Solution:
    def threeSum(self, arr):
        n = len(arr)
        ans = set()
        result = []

        for i in range(n):
            hashset = set()

            for j in range(i + 1, n):
                third = -(arr[i] + arr[j])

                if third in hashset:
                    triplet = tuple(sorted([arr[i], arr[j], third]))
                    ans.add(triplet)

                hashset.add(arr[j])

        for triplet in ans:
            result.append(list(triplet))

        return result