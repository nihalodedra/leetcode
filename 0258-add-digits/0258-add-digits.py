class Solution:
    def addDigits(self, n: int) -> int:
        while n>=10:
            x = n % 10
            y = n // 10
            n = x + y
        return n
        