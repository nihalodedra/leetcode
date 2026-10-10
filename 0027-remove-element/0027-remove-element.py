class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        l = []
        for i in nums:
            if i != val:
                l.append(i)

        n = len(l)
        nums[:n] = l

        return n