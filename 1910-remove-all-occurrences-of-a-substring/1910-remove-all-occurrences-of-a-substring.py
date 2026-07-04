class Solution(object):
    def removeOccurrences(self, s, part):

        while part in s:
            idx = s.find(part)
            s = s[:idx] + s[idx + len(part):]

        return s