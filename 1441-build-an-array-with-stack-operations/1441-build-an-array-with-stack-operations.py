class Solution(object):
    def buildArray(self, target, n):
        stack = []
        j = 0

        for i in range(1, n + 1):
            if j == len(target):
                break

            stack.append("Push")

            if i == target[j]:
                j += 1
            else:
                stack.append("Pop")

        return stack
       

        
        