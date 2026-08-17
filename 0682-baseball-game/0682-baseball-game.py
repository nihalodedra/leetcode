class Solution:
    def calPoints(self, o: List[str]) -> int:
        s = []
        for i in o:
            if i == "+":
                s.append(s[-1]  + s[-2])
            elif i == "D":
                s.append(2*s[-1])
            elif i == "C":
                s.pop()
            else:
                s.append(int(i))
        return sum(s)

      