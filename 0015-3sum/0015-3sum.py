class Solution:
    def threeSum(self, arr: list[int]) -> list[list[int]]:
        ans=[]
        arr.sort()
        n=len(arr)
        for i in range(n):
            if i !=0 and arr[i] == arr[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                tsum = arr[i]+arr[j]+arr[k]
                if tsum<0:
                    j+=1
                elif tsum>0:
                    k-=1
                else:
                    temp=[arr[i],arr[j],arr[k]]
                    ans.append(temp)
                    j+=1
                    k-=1
                    while j<k and arr[j]==arr[j-1]:
                        j+=1
                    while j<k and arr[k]==arr[k+1]:
                        k-=1
        return ans