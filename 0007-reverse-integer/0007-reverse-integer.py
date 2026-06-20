class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversed_num = 0
        is_pos = 1
        if x < 0:
            is_pos = 0
            x = -x
        
        while x > 0:
            digit = x % 10                
            reversed_num = (reversed_num * 10) + digit  
            x= int(x / 10)

        if reversed_num > 2**31 -1 or reversed_num<=-2**32:
            return 0
            
        if is_pos == 0:
            return -reversed_num
        else:
            return reversed_num

