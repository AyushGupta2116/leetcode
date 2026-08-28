class Solution(object):
    def minOperations(self, nums):
        st = []
        count = 0

        for i in nums:

            while st and st[-1] > i:
                st.pop()

            if i == 0:
                continue

            if not st or st[-1] < i:
                st.append(i)
                count += 1

        return count
            

        