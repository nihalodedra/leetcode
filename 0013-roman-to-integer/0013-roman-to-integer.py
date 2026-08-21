class Solution:
    def romanToInt(self, s: str) -> int:
        l = len(s)
        total = 0
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M =  1000
        for i in range(l):
            c_var = locals()[s[i]]

            if i < l-1:
                n_var = locals()[s[i+1]]

                if c_var < n_var:
                    total -=c_var
                else:
                    total +=c_var
            else:
                    total +=c_var
        return total


        