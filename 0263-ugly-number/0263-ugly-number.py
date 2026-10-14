class Solution:
    def isUgly(self, n: int) -> bool:
        ans = [2,3,5]
        if n<=0:
            return False
        for i in ans:
            while n%i ==0:
                n=n//i
        return n == 1