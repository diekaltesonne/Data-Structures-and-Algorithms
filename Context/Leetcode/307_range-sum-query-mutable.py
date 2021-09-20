# https://www.youtube.com/watch?v=v_wj_mOAlig
# https://neerc.ifmo.ru/wiki/index.php?title=%D0%94%D0%B5%D1%80%D0%B5%D0%B2%D0%BE_%D0%A4%D0%B5%D0%BD%D0%B2%D0%B8%D0%BA%D0%B0
# http://e-maxx.ru/algo/fenwick_tree
# [Binary Indexed Tree.py](https://gist.github.com/rajatdiptabiswas/79fc1ce5cf410df4139b291f75bf0794)
from typing import List

class Fenwik_Tree:
    def __init__(self, len_of_nums: int, nums: List ):
        self.len_of_nums  = len_of_nums
        self.t = [0 for i in range (self.len_of_nums+1)]
        self.build(nums)

    def modify(self, i, d):
        i+=1
        while i < self.len_of_nums+1:
            self.t[i] += d
            i += i & -i
    
    def build(self, nums: List):
        for i in range(0,self.len_of_nums):
            self.modify(i, nums[i])
    
    def sum(self, i: int) -> int:
        i += 1
        result = 0
        while i > 0:
            result += self.t[i]
            i -= i & -i
        return result
    
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.ftree = Fenwik_Tree(len(nums),self.nums)
    
    def update(self, index: int, val: int) -> None:
        d = val - self.nums[index]
        self.nums[index] = val
        self.ftree.modify(index, d)

    def sumRange(self, left: int, right: int) -> int:
        return self.ftree.sum(right) - self.ftree.sum(left-1)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

def main ():
   obj = NumArray([-1])
   print(obj.sumRange(0,0))
   obj.update(0,1)
   print(obj.sumRange(0,0))

if __name__ == "__main__":
    main()