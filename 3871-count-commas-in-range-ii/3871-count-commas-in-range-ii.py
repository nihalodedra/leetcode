class Solution:
    def countCommas(self, n: int) -> int:
        c=0
        t=1000
        while t<=n:
            c+=n-t+1
            t*=1000
        return c
            
        