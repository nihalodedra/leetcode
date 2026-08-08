class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        nums.sort()
        max_d = 0
        for i in range(0,len(nums)-1):
            diffrance=nums[i+1]-nums[i]
            if diffrance > max_d:
                max_d = diffrance
        return max_d
