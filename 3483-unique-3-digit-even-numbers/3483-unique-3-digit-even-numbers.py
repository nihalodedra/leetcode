from typing import List

class Solution:
    def totalNumbers(self, d: List[int]) -> int:
        s = set()
        l = len(d)
        for i in range(l):
            for j in range(l):
                for k in range(l):
                    if i!= j and j!=k and i!=k:
                        if d[i] !=0:
                            if d[k]%2==0:
                                num = d[i]*100+d[j]*10+d[k]
                                s.add(num)
        return len(s)