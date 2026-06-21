class Solution(object):
    def shuffle(self, nums, n):
        list1 = nums[:n]
        list2 = nums[n:]

        k = []

        for i in range(n):
            k.append(list1[i])
            k.append(list2[i])

        return k