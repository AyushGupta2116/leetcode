class Solution(object):
    def maxProduct(self, n):
        m = sorted(str(n))
        l = len(m)
        return int(m[l-1]) * int(m[l-2])
        

        