class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        ans=0
        n=len(s)
        last = -1
        for i in range(2*n-1):
            l=i//2
            r=l+(i%2)
            while l>=0 and r<n and s[l]==s[r]:
                if l>last and (r-l+1) >=k:
                    ans +=1
                    last = r
                    break
                l-=1
                r+=1
        return ans