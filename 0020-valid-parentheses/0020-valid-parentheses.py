class Solution(object):
    def isValid(self, s):
        stack=[]
        pairs={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        empty=[]
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if stack==empty:
                    return False
                if stack[-1]!=pairs[i]:
                    return False
                stack.pop()
        return len(stack)==0