class Solution:
    def maxDepth(self, s: str) -> int:
        curd = 0
        maxd =0 
        for char in s:
            if char == "(":
                curd+=1
                maxd=max(maxd,curd)
            elif char == ")":
                curd-=1
        return maxd


        