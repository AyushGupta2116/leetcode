class Solution(object):
    def halvesAreAlike(self, s):
        n = len(s)
        a = s[:n/2]
        b = s[n/2:n]
        vowels = "aeiouAEIOU"
        count0= 0
        count1= 0
        for i in a:
            if i in vowels:
                count0 += 1
        for j in b:
            if j in vowels:
                count1 += 1
        return count0==count1
        