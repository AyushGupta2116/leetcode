class Solution(object):
    def generateParenthesis(self, n):

        result = []

        def solve(curr, open, close):

            if len(curr) == 2 * n:
                result.append("".join(curr))
                return

            if open < n:
                curr.append("(")
                solve(curr, open + 1, close)
                curr.pop()

           
            if close < open:
                curr.append(")")
                solve(curr, open, close + 1)
                curr.pop()

        curr = []
        solve(curr, 0, 0)

        return result
        
        