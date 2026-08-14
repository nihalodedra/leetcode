class Solution:
    def moveZeroes(self, n: List[int]) -> None:
        count=0
        for i in range(0,len(n)):
            if n[i] != 0:
                n[count] , n[i] = n[i],n[count]
                count+=1
            
        """
        Do not return anything, modify nums in-place instead.
        """
        