class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        tsum = 0
        for i in range(n):
            element = set()
            for j in range(i, n):
                element.add(nums[j])
                tsum += len(element)**2
        return tsum