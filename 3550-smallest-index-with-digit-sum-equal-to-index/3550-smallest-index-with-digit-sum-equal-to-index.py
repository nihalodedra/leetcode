class Solution(object):
    def smallestIndex(self, nums):
        for i in range (len(nums)):
            summ = 0
            while nums[i]>0:
                summ+= nums[i]%10
                nums[i]=nums[i]//10
            if summ==i:
                return i
        return -1