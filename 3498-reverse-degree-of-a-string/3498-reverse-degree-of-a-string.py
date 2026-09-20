class Solution:
    def reverseDegree(self, s: str) -> int:
        n = len(s)
        total=0
        for i in range(0,n):
            v = ord('z')-ord(s[i])+1
            p = i+1
            total+=v*p
        return total

