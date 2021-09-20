from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class SolutionOld:
    def isSameTree(self, p, q):    
        if not p and not q:
            return True
        if not q or not p:
            return False
        return (p.val == q.val) and self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)
               

class Solution(SolutionOld):
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isSameTree(root,root)


def main():
    a = Solution()
    p = [1,2] 
    q = [1,None,2]
    print(a.isSameTree(p,q))

if __name__ == "__main__":
    main()