class Solution:
    def maxProfit(self, p: List[int]) -> int:
        l = 0
        r=1
        max_=0
        while r<len(p):
            if p[l]<p[r]:
                pro=p[r]-p[l]
                max_ = max(max_,pro)
            else:
                l = r
            r+=1
        return max_