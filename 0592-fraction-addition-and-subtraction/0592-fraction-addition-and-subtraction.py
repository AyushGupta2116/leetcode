
class Solution(object):

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def fractionAddition(self, expression):

        num = 0
        den = 1
        i = 0

        while i < len(expression):

            sign = 1
            if expression[i] == '+':
                i += 1
            elif expression[i] == '-':
                sign = -1
                i += 1

            n = 0
            while expression[i].isdigit():
                n = n * 10 + int(expression[i])
                i += 1

            i += 1      

            d = 0
            while i < len(expression) and expression[i].isdigit():
                d = d * 10 + int(expression[i])
                i += 1

            num = num * d + sign * n * den
            den = den * d

            g = self.gcd(abs(num), den)
            num //= g
            den //= g

        return str(num) + "/" + str(den)