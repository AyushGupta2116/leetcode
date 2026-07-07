class Solution(object):
    def countHomogenous(self, s):
        mod = 10**9 + 7

        length = 0
        result = 0

        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                length += 1
            else:
                length = 1

            result += length

        return result % mod
         
        