class Solution:
    def minMoves(self, n: List[int]) -> int:
        return len(n)*max(n) - sum(n)
        