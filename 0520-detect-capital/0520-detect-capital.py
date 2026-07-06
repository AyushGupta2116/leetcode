class Solution(object):
    def detectCapitalUse(self, word):
        if word.istitle():
            return True
        elif word.islower():
            return True
        elif word.isupper():
            return True
        else:
            return False
        
