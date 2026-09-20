class Solution(object):
    def reversePrefix(self, word, ch):
        l = word.find(ch)

        if l == -1:
            return word

        arr = list(word)

        arr[:l+1] = arr[:l+1][::-1]

        return "".join(arr)

        