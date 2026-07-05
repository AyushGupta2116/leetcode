class Solution(object):
    def reverseWords(self, s):
        s = s[::-1]
        ans = ""

        i = 0
        while i < len(s):
            word = ""

            while i < len(s) and s[i] == " ":
                i += 1

            while i < len(s) and s[i] != " ":
                word += s[i]
                i += 1

            word = word[::-1]

            if len(word) > 0:
                if ans:
                    ans += " "
                ans += word

        return ans