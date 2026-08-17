class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        for b in s:
            if b =="(" or b == "{" or b== "[":
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                d = stack.pop()
                if (    (b == ")" and d =="(") or (b == "}" and d =="{") or (b == "]" and d =="[")     ):
                    continue
                    return True
                else:
                    return False
        return len(stack) == 0