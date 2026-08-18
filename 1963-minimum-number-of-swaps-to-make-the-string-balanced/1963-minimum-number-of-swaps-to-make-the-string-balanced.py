class Solution(object):
    def minSwaps(self, s):
        stack = []

        for i in s:
            if i == "[":
                stack.append(i)

            elif i == "]":
                if stack:
                    stack.pop()

        return (len(stack) + 1) // 2


      
        