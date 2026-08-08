class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n=len(citations)
        count=0
        for i in range(n):
            rp = n-i
            if citations[i]>=rp:
                return rp
        return 0
            
        


        