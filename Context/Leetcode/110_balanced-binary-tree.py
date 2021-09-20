# Definition for a binary tree node.
import math
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return False
        if root.left is not None:
            x
            x = isBalanced(root.left)
        if root.right is not None:
            y = isBalanced(root.left)
        return x and y


def creatBTree(data, index):
    pNode = None
    if index < len(data):
        if data[index] == None:
            return
        pNode = TreeNode(data[index])
        pNode.left = creatBTree(data, 2 * index + 1) # [1, 3, 7, 15, ...]
        pNode.right = creatBTree(data, 2 * index + 2) # [2, 5, 12, 25, ...]
    return pNode


def main():

    a = Solution()
    root = [3,9,20,None,None,15,7]
    root1 = [1,2,3,4,None,None,5]  
    print(a.maxDepth(creatBTree(root1,0)))
    print(a.ans_opt)

if __name__ == "__main__":
    main()