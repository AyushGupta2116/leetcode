class Solution(object):
    def checkInclusion(self, s1, s2):
        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        checks1 = sorted(s1)

        
        for i in range(m - n + 1):
            temp = s2[i:i + n]     
            if sorted(temp) == checks1:
                return True

        return False