class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return""
        prifix = strs[0]
        for i in range(1,len(strs)):
            while not strs[i].startswith(prifix):
                prifix = prifix[:-1]

                if  not prifix:
                    return""
        return prifix
            
        