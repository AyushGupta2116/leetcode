class Solution(object):
    def countSubstrings(self, s, c):
        count =0
        substr = 0
        for i in range(len(s)):
            if s[i]== c:
                substr += (1+count)
                count +=1
        return substr
        
        