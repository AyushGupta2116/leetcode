class Solution(object):

    def nCr(self, n, r):
        res = 1

        for i in range(r):
            res = res * (n - i)
            res = res / (i + 1)

        return res

    def generate(self, numRows):
        ans = []

        for i in range(numRows):
            row = []

            for j in range(i + 1):
                row.append(self.nCr(i, j))

            ans.append(row)

        return ans