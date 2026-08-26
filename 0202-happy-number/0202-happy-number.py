class Solution:
    def isHappy(self, n: int) -> bool:
        while n!=1 and n!=4:
            total = 0
            for d in str(n):
                total+=int(d)*int(d)
            n = total
        return n == 1
        