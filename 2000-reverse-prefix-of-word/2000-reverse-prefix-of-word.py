class Solution(object):
    def reversePrefix(self, word, ch):
        l = word.find(ch)
        result = ""

        for i in range(l, -1, -1):
            result += word[i]

        for i in range(l + 1, len(word)):
            result += word[i]

        return result

        