class Solution:
    def fourSum(self, arr, target):
        n = len(arr)
        arr.sort()
        ans = []

        for i in range(n):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue

                k, l = j + 1, n - 1
                while k < l:
                    sum = arr[i] + arr[j] + arr[l] + arr[k]

                    if sum == target:
                        ans.append([arr[i], arr[j], arr[k], arr[l]])

                        while k < l and arr[k] == arr[k + 1]:
                           k += 1
                        while j < l and arr[l] == arr[l - 1]:
                           l -= 1

                        k += 1
                        l -= 1
                    elif sum < target:
                        k += 1
                    else:
                        l -= 1
        return ans
