class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        n = len(s)
        start = 0 
        end = n-1
        while start<end:
            if not s[start].isalnum():
                start+=1
            elif not s[end].isalnum():
                end-=1
            elif s[start]!= s[end]:
                return False
            else:
                start+=1
                end-=1
        return True