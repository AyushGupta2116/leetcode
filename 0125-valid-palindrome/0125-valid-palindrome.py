class Solution(object):
    def isPalindrome(self, s):

        s = s.lower()
        start = 0
        end = len(s) - 1

        def alphanumeric(ch):
            if ('0' <= ch <= '9') or ('a' <= ch <= 'z'):
                return True
            return False

        while start < end:

            if not alphanumeric(s[start]):
                start += 1
                continue

            if not alphanumeric(s[end]):
                end -= 1
                continue

            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True