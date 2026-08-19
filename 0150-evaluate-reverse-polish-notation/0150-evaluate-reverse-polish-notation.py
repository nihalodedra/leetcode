class Solution:
    def evalRPN(self, t: List[str]) -> int:
        stack =[]
        for i in t:
            if i == "+":
                stack.append(stack.pop()+stack.pop())
            elif i == "-":
                n=stack.pop()
                d=stack.pop()
                stack.append(d-n)
            elif i == "*":
                stack.append(stack.pop()*stack.pop())
            elif i == "/":
                a=stack.pop()
                b=stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(i))
        return stack[0]

        