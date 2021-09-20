class Solution:
    def romanToInt(self, s: str) -> int:
        num = []
        ans = 0
        check = 0
        symbols ={"I":1,
                "V":5,
                "X":10,
                "L":50,
                "C":100,
                "D":500,
                "M":1000,}
        
        for symb in s:
            num.append(symbols[symb])
        
        for i in range(len(num)):
            if i != len(num)-1:
                if num[i] < num[i+1]:
                    check = num[i]
                else:
                    num[i] = num[i] - check 
                    ans = ans + num[i]
                    check = 0 
            else:
                num[i] = num[i] - check 
                ans = ans + num[i]

        return ans
