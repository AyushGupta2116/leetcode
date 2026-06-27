class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"

        negative = num < 0
        num = abs(num)

        m = ""

        while num > 0:
            m = m + str(num % 7)
            num = int (num/7)

        m = m[::-1]

        if negative:
            m = "-" + m

        return m
        