class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        n = len(s)

        while n > 0 and s[n-1] == ' ':
            n -= 1

        while n > 0 and s[n-1] != ' ':
            count += 1
            n -= 1

        return count




        
        

        