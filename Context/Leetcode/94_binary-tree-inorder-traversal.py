# [Tree Traversals (Inorder, Preorder and Postorder)]
# (https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/)
# [Oбход дерева – центрированный (inorder), прямой (preorder) и обратный (postorder) (три основных способа обхода)](
# https://evileg.com/ru/post/490/)
# Definition for a binary tree node.

from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return []
        ans.extend(self.inorderTraversal(root.left))
        ans.append((root.val))
        ans.extend(self.inorderTraversal(root.right))
        return ans

        

def main():

    a = Solution()
    root = [1,None,2,3]
    a.inorderTraversal(root)
    print(root)

if __name__ == "__main__":
    main()