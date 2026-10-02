class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []
        def backtrack(ope,clo):
            if ope == clo == n:
                res.append("".join(stack))
                return
            if ope<n:
                stack.append("(")
                backtrack(ope+1,clo)
                stack.pop()

            if clo<ope:
                stack.append(")")
                backtrack(ope,clo+1)
                stack.pop()
        backtrack(0,0)
        return res
                
            
        