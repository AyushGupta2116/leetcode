class Solution(object):
    def numberOfSpecialChars(self, s):
        s = list(set(s))      
        count = 0

        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if abs(ord(s[i]) - ord(s[j])) == 32:
                    count += 1

        return count

        
        