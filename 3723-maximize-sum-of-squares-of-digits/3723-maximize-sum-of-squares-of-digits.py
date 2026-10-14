class Solution:
    def maxSumOfSquares(self, n: int, s: int) -> str:
        if s== 0 or s>n*9:
            return ""
        nines = s//9
        rem = s%9

        res=['9']*nines
        if rem>0:
            res.append(str(rem))
        zero = n - len(res)
        res.extend(['0']*zero)
        return "".join(res)