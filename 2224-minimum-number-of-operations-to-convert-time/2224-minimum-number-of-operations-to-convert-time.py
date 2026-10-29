class Solution(object):
    def convertTime(self, current, correct):
        hr1 = int(current[:2])
        m1 = int(current[3:])

        hr2 = int(correct[:2])
        m2 = int(correct[3:])

        t1 = hr1 * 60 + m1
        t2 = hr2 * 60 + m2

        diff = t2 - t1
        count = 0

        for i in [60, 15, 5, 1]:
            count += diff // i
            diff %= i

        return count

           
       
        