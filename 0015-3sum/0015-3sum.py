class Solution:
    def threeSum(self, arr):
        n = len(arr)
        arr.sort()
        ans = []

        for i in range(n):

            if i > 0 and arr[i] == arr[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:

                sum = arr[i] + arr[j] + arr[k]

                if sum == 0:
                    ans.append([arr[i], arr[j], arr[k]])

                    j += 1
                    k -= 1

                    
                    while j < k and arr[j] == arr[j- 1]:
                        j += 1

                    
                    while j < k and arr[k] == arr[k + 1]:
                        k-= 1

                elif sum < 0:
                    j += 1

                else:
                    k -= 1

        return ans
