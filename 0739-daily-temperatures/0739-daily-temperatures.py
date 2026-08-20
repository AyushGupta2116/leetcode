class Solution(object):

    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ans = [0] * n
        hot = 0

        for i in range(n - 1, -1, -1):
            curr = temperatures[i]

            if curr >= hot:
                hot= curr
            else:
                days = 1
                
                while temperatures[i + days] <= curr:
                    days += ans[i + days]
                ans[i] = days
        
        return ans

            

           
          

       
        