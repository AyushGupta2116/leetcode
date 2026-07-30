class Solution(object):
    def minimumPushes(self, word):
        ans =0
        for i in range(0,len(word)):
            ans+= (i/8)+1
        return ans


        