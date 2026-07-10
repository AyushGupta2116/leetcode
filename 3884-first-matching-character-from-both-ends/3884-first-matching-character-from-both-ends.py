class Solution(object):
    def firstMatchingIndex(self, s):
        i =0 
        j = len(s)
        while i<len(s) and j>0:
            if s[i] == s[j-1]:
                return i
                break
            else:
                i +=1
                j -=1
        return -1
        
        