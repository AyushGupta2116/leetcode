class Solution(object):
    def checkIfPangram(self, stri):

        seen = [False] * 26

        for i in range(len(stri)):
            indx = ord(stri[i]) - ord('a')
            seen[indx] = True

        for j in seen:
            if j == False:
                return False

        return True

