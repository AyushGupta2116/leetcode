class Solution(object):
    def repeatedSubstringPattern(self, s):
        temp = s + s
        temp = temp[1:-1]

        if s in temp:
            return True
        else:
            return False

        
         