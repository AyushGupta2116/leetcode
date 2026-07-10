class Solution(object):
    def reverseVowels(self, s):
        vowels = "aeiouAEIOU"
        arr = []

        for i in s:
            if i in vowels:
                arr.append(i)

        arr = arr[::-1]

        s = list(s)
        i = 0
        j = 0

        while i < len(s):
            if s[i] in vowels:
                s[i] = arr[j]
                j += 1
            i += 1

        return "".join(s)
                
            


          
        