class Solution(object):
    def repeatedSubstringPattern(self, s):
        n = len(s)

        for l in range(n // 2, 0, -1):
            if n % l == 0:
                times = n // l
                substr= s[:l]

                if substr * times == s:
                    return True

        return False
       

        
         