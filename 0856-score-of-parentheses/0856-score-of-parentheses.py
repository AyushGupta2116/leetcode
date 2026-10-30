class Solution(object):
    def scoreOfParentheses(self, s):
        st = []
        res = 0

        for i in s:
            if i == '(':
                st.append(res)
                res = 0
            else:
                res = st.pop() + max(res * 2, 1)

        return res
        