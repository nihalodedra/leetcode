class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(s):
            stack = []
            for i in s:
                if i == "#" and stack:
                    stack.pop()
                elif  i!= "#":
                    stack.append(i)
            return stack
        return helper(s) == helper(t)