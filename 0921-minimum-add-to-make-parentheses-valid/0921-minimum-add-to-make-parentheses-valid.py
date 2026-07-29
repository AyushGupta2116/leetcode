class Solution(object):
    def minAddToMakeValid(self, s):
        valid = 0
        ans = 0

        for i in s:
            if i == "(":
                valid += 1
            else:
                if valid> 0:
                    valid-= 1
                else:
                    ans += 1

        return ans + valid

        