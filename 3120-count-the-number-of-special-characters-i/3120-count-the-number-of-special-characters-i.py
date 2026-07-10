class Solution(object):
    def numberOfSpecialChars(self, s):
        st = set(s)
        count = 0
        m = "abcdefghijklmnopqrstuvwxyz"

        for i in m:
            if i in st and i.upper() in st:
                count += 1

        return count

        
        