class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
         return False

        original = x
        reversed_num = 0

        while x > 0:
            digit = x % 10
            reversed_num = (reversed_num * 10) + digit
            x = int(x / 10)

        if original == reversed_num:
            return True
        else:
            return False