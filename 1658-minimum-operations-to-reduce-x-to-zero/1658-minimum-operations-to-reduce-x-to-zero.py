class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        tar = sum(nums)-x
        cursum = 0
        maxw_ = -1
        l=0
        for r in range(len(nums)):
            cursum += nums[r]
            while l<=r and cursum > tar:
                cursum -= nums[l]
                l+=1
            if cursum == tar:
                maxw_=max(maxw_,r-l+1)

        if maxw_==-1:
            return maxw_
        else:
            return len(nums)-maxw_