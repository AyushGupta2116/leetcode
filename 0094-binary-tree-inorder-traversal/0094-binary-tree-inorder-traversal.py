class Solution(object):
    def inorderTraversal(self, root):
        ans = []

        def solve(root):
            if root is None:
                return

            solve(root.left)
            ans.append(root.val)
            solve(root.right)

        solve(root)

        return ans