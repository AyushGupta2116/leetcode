class Solution(object):
    def sumAndMultiply(self, n):
        sum = 0
        arr = []

        for i in str(n):
            if i != '0':
                sum += int(i)
                arr.append(i)

        x = int("".join(arr)) if arr else 0

        return x * sum