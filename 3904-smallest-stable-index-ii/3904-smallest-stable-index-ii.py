class Solution:
    def firstStableIndex(self, n: list[int], k: int) -> int:
        l = len(n)
        if l == 0:
            return -1
        min_ = n.copy()
        for i in reversed(range(l-1)):
            if min_[i+1]<min_[i]:
                min_[i]=min_[i+1]
        max_=n[0]
        for i in range(l):
            if n[i]>max_:
                max_=n[i]
            if max_ - min_[i] <= k:
                return i
        return -1
        