class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = format(n,'b')
        c=0
        for char in ans:
            if char =='1':
                c+=1
        return c
        