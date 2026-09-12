class Solution:
    def arrangeCoins(self, n: int) -> int:
        l =0
        r=n
        while l<=r:
            m =l+(r-l)//2
            cn=(m*(m+1))//2
            if cn ==n:
                return m
            elif cn <n:
                l=m+1
            else:
                r=m-1
        return r