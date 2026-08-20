class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        a = [0] * n
        stack = []
        for i in range(n):
            while stack and t[i]>t[stack[-1]]:
                j = stack.pop()
                a [j]= i -j
            stack.append(i)
        return a

        