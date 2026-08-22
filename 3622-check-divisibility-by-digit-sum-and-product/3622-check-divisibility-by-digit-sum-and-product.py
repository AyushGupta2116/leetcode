class Solution(object):
    def checkDivisibility(self, n):
        orig=n
        sum =0
        pdt =1
       
        while n>0:
            m = n%10
            n = n//10
            sum +=m
            pdt *=m

       
        if orig % (sum+pdt) == 0:
            return True
        else:
            return False

    

        

        
        