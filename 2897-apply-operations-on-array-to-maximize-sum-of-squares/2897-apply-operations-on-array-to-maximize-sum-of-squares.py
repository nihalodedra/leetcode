class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mod = 10**9 +7
        cnt = [0]*31
        for num in nums:
            for i in range(31):
                if num & (1<<i):
                    cnt[i]+=1
        res =0
        for n in range(k):
            cur = 0
            for j in range(30,-1,-1):
                if cnt[j]>0:
                    cur |= 1<<j
                    cnt[j] -=1
            res = (res+cur*cur)%mod
        return res  