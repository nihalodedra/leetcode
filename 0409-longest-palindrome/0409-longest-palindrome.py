class Solution:
    def longestPalindrome(self, s: str) -> int:
        ul = set()
        l = 0
        for let in s:
            if let in ul:
                ul.remove(let)
                l += 2
            else:
                ul.add(let) 
        if ul:
            l += 1
        return l