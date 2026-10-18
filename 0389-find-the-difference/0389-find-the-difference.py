class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = 0
        for i in s + t:
            counter ^= ord(i)
        return chr(counter)
        