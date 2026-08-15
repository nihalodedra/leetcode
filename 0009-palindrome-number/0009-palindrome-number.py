class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        x2 = str(x)[::-1]
        if x == x2:
            return True
        else:
            return False
        