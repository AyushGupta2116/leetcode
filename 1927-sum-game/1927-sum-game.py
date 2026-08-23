class Solution(object):
    def sumGame(self, num):
        n = len(num)
        diff = 0
        q = 0

        for i in range(n // 2):
            if num[i] == '?':
                q += 1
            else:
                diff += int(num[i])

        for i in range(n // 2, n):
            if num[i] == '?':
                q -= 1
            else:
                diff -= int(num[i])

        return q % 2 != 0 or diff != -(q // 2) * 9