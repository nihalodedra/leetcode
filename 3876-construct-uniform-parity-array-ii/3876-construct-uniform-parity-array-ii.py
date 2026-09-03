class Solution:
    def uniformArray(self, n1: list[int]) -> bool:
        min_ =min(n1)
        if min_%2 != 0:
            return True
        only_even = any(x%2 !=0 for x in n1)
        return not only_even
        