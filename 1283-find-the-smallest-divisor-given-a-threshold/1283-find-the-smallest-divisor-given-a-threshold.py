class Solution:
    def smallestDivisor(self, n: List[int], t: int) -> int:
        l=1
        r=max(n)
        while(l<=r):
            m=l+(r-l)//2
            cs = sum((num + m -1)//m for num in n)
            if cs >t:
                l = m +1
            else:
                r = m -1
        return l
        