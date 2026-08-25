class Solution:
    def merge(self, n1: List[int], m: int, n2: List[int], n: int) -> None:
         n1[m:] = n2
         n1.sort()
        