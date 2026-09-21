class Solution(object):
    def reverseDegree(self, s):
        sum = 0

        for i, j in enumerate(s, 1):
            value = ord('z') - ord(j) + 1
            sum += i * value

        return sum
        
        