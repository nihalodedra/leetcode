class Solution:
    def targetIndices(self, n: list[int], t: int) -> list[int]:
        l = []
        n.sort()
        for i in range(len(n)):
            if n[i] == t:
                l.append(i)
        return l

        