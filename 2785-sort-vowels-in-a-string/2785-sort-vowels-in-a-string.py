class Solution(object):
    def sortVowels(self, s):
        vowels = "aeiouAEIOU"

        arr = []

        for i in s:
            if i in vowels:
                arr.append(i)

        arr.sort()

        s = list(s)
        k = 0

        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = arr[k]
                k += 1

        return "".join(s)