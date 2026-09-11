class Solution(object):
    def totalNumbers(self, digits):
        count = 0

        for num in range(100, 1000, 2):
            temp = list(digits)
            possible = True

            for d in str(num):
                d = int(d)

                if d in temp:
                    temp.remove(d)
                else:
                    possible = False
                    break

            if possible:
                count += 1

        return count