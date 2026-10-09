class Solution:
    def minInsertions(self, s: str) -> int:
        count1 = 0
        count2=0
        for ch in s:
            if ch == "(":
                count1 += 2
                if count1 %2 ==1:
                    count1 -=1
                    count2 +=1 
            elif ch == ")":
                count1 -=1
                if count1 <0:
                    count2+=1
                    count1 = 1
        ans = count1+count2
        return ans