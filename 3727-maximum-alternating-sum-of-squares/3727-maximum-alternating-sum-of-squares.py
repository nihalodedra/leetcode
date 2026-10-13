class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range (n):
            nums[i] = (nums[i] *nums[i])
        nums.sort()
        mid = n//2
        first = sum(nums[:mid]) 
        second = sum(nums[mid:])
        return second - first
        