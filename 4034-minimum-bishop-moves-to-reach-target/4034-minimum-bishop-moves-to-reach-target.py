class Solution(object):
    def minBishopMoves(self, source, target):
        r1,c1 = source
        r2,c2 = target
        if r1 ==r2 and c1==c2:
            return 0
        if abs(r1-r2)== abs(c1-c2):
            return 1

        if (r1+c1) %2 == (r2+c2) %2:
            return 2

        return -1
        
        
        