class Solution(object):
    def numSub(self, s):
        ans = 0
        count = 0
        mod = 10**9 + 7

        for i in s:
            if i == '1':
                count += 1
                ans += count
            else:
                count = 0

        return ans % mod
        
        