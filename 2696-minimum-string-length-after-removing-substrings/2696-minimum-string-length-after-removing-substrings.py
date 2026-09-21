class Solution(object):
    def minLength(self, s):
        stack = []

        for i in s:
            stack.append(i)

            if len(stack) >= 2:
                if stack[-2] + stack[-1] in ('AB', 'CD'):
                    stack.pop()
                    stack.pop()

        return len(stack)
            




    
        
        