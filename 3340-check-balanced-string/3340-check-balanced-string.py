class Solution(object):
    def isBalanced(self, num):
        sum =0
        sum1=0
        for i in range (0,len(num),2):
            sum = sum+int(num[i])

        for j in range (1,len(num),2):
            sum1 = sum1 + int(num[j])

        if sum==sum1:
            return True
        else:
            return False