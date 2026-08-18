class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and i == stack[-1]:
                stack.pop()
            elif i != stack:
                stack.append(i)
        return "".join(stack)
        