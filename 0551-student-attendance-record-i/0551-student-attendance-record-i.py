class Solution(object):
    def checkRecord(self, s):
        count =0
        count1 =0
        maxi =0
        for i in s:
            if i == 'A':
                count +=1
        for i in s:
            if i == 'L':
                count1 +=1
                maxi = max(maxi,count1)
            else:
                count1 =0

        if count<2 and maxi<3:
            return True
        else:
            return False

        