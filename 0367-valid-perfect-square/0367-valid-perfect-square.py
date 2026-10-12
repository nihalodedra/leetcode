class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        l = 2
        r = num//2
        while l<=r:
            mid = l+(r-l)//2
            g = mid*mid

            if g == num:
                return True
            elif g<num:
                l = mid +1
            else:
                r = mid - 1
        return False
