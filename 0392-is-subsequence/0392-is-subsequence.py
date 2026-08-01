class Solution(object):
    def isSubsequence(self, s, t):
        m = len(s)
        n = len(t)
        i=0
        j=0
        while i<m and j<n:
            if s[i]==t[j]:
                i+=1
            j+=1
        
        if i==m:
            return True
        else:
            return False
        