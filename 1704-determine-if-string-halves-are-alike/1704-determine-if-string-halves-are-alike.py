class Solution(object):
    def halvesAreAlike(self, s):
        vowels = "aeiouAEIOU"

        count1 = 0
        count2 = 0
        n = len(s)

        for i in range(n // 2):
            if s[i] in vowels:
                count1 += 1

        for i in range(n // 2, n):
            if s[i] in vowels:
                count2 += 1

        if count1 == count2:
            return True
        else:
            return False