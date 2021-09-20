from typing import List
# - [How to Convert a Python String to int](https://realpython.com/convert-python-string-to-int/)

class Solution_1:
    root = 0
    counter = 0 
    def climbStairsrec (self, n: int, sum: int, num: int) -> int:
        if sum + num < n:
            self.climbStairsrec(n,sum + num,1)
            self.climbStairsrec(n,sum + num,2)
        if sum + num == n:
            self.counter += 1

    def climbStairs(self, n: int) -> int:
        self.climbStairsrec(n,0,1)
        self.climbStairsrec(n,0,2)
        a = self.counter
        self.counter = 0
        return a
    
class Solution_2:
    def climbStairs(self, n: int) -> int:
        steps = [0 for i in range(n)]        
        steps[0]=1
        steps[1]=2
        for i in range(2,len(steps)):
            steps[i] = steps[i-1] +steps[i-2]
        return steps[n - 1]
class Solution:
    root = 0

    def climbStairsrec (self, n: int, sum: int, num: int) -> int:
        if sum + num > n:
            return 0
        if sum + num < n:
            return self.climbStairsrec(n,sum + num,1)+self.climbStairsrec(n,sum + num,2)
        if sum + num == n:
            return 1

    def climbStairs(self, n: int) -> int: 
        return self.climbStairsrec(n,0,1)+self.climbStairsrec(n,0,2)

def main():
    a = Solution_2()
    print(a.climbStairs(n = 29))
    print(a.climbStairs(n = 3))



if __name__ == "__main__":
    main()