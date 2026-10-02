class Solution(object):
    def generateParenthesis(self, n):
        result = []
        curr = []

        def valid():
            count = 0

            for i in curr:
                if i == '(':
                    count += 1
                else:
                    count -= 1

                if count < 0:
                    return False

            return count == 0

        def solve():
            if len(curr) == 2 * n:
                if valid():
                    result.append("".join(curr))
                return

            curr.append("(")
            solve()
            curr.pop()

            curr.append(")")
            solve()
            curr.pop()

        solve()

        return result

        
        