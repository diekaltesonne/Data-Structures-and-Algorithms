from typing import List
# [Methods of computing square roots](https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method)
# [Babylonian method for square root](https://www.geeksforgeeks.org/square-root-of-a-perfect-square/)
#1 Start with an arbitrary positive start value x (the closer to the 
#   root, the better).
#2 Initialize y = 1.
#3. Do following until desired approximation is achieved.
#  a) Get the next approximation for root using average of x and y
#  b) Set y = n/x

class Solution:
    def mySqrt(self, x: int) -> int:
        k = x
        y = 1
        e = 0.000001
        while(k-y > e):
            k = (k+y)/2
            y = x/k

        return int(k)

def main():
    a = Solution()
    print(a.mySqrt(x = 4))
    print(a.mySqrt(x = 8))



if __name__ == "__main__":
    main()