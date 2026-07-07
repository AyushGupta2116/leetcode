class Solution(object):
    def buddyStrings(self, s, goal):

        if len(s) != len(goal):
            return False

        if s == goal:
            return len(set(s)) < len(s)

        temp = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                temp.append(i)

        if len(temp) != 2:
            return False

        i, j = temp

        return s[i] == goal[j] and s[j] == goal[i]

        return s[i] == goal[j] and s[j] == goal[i]
                   