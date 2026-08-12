class Solution(object):
    def maximum69Number (self, n):
        n = [int(num) for num in str(n)]
        for i in range(len(n)):
            if n[i] == 6:
                n[i] = 9
                break
        return int("".join(map(str,n)))