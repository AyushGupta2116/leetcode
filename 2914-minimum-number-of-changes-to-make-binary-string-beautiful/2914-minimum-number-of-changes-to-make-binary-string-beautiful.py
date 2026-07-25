class Solution(object):
    def minChanges(self, s):
        n = len(s)
        change =0
        for i in range(0,n,2):
            if s[i]!=s[i+1]:
                change+=1

        return change
        


        


        