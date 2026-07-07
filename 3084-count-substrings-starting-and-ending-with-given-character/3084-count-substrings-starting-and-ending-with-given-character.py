class Solution(object):
    def countSubstrings(self, s, c):
        n = s.count(c)
        nc2 = (n * (n-1)) /2

        return n + nc2
        
        