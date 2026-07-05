class Solution(object):
    def appendCharacters(self, s, t):
        m = len(s)
        n = len(t)
        i =0 
        j =0

        while(i<m and j<n):
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                i+=1

        return n-j


        