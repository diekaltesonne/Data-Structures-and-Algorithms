from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = 0
        
        if digits[-1] + 1 >= 10:
            digits[-1]+=1
            for i in range(len(digits)-1,-1,-1):
                digits[i]+=a
                if digits[i] >= 10:
                    digits[i] = 0
                    a =1 
                else:
                    a =0
            if digits[0]==0:
                digits = [1] + digits
                return digits
            else:
                return digits        
        else:   
            digits[-1]+=1
            return digits

def main():
    a = Solution()
    print(a.plusOne(digits = [9,9,9]))
    print(a.plusOne(digits = [4,3,2,1]))
    print(a.plusOne(digits = [0]))


if __name__ == "__main__":
    main()