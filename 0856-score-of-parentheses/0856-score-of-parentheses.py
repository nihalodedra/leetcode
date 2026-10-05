class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        count = 0
        dep=0
        for i,char in enumerate(s):
            if char == "(":
                dep +=1
            else:
                dep -=1
                if s[i-1]=="(":
                    count +=1<<dep
        return count