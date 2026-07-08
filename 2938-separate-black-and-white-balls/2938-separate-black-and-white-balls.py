class Solution(object):
    def minimumSteps(self, s):
        count1 = 0
        ans = 0

        for i in s:
            if i == '1':
                count1 += 1
            else:
                ans += count1

        return ans
        
        

        