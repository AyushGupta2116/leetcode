class Solution(object):
    def appendCharacters(self, s, t):
        j = 0
        m = len(t)
        for i in s:
            if i == t[j]:
                j += 1
                if j == m:
                    return 0
        return m - j
        




        