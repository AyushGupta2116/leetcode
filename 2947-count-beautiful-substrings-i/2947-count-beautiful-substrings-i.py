class Solution(object):
    def beautifulSubstrings(self, s, k):
        result = 0
        vowel = "aeiou"

        for i in range(len(s)):
            vowels = 0
            cons = 0

            for j in range(i, len(s)):
                if s[j] in vowel:
                    vowels += 1
                else:
                    cons += 1

                if vowels == cons and (vowels * cons) % k == 0:
                    result += 1

        return result
        
        