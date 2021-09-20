# Definition for a binary tree node.
import math
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
def creatBTree(data, index):
    pNode = None
    if index < len(data):
        if data[index] == None:
            return
        pNode = TreeNode(data[index])
        pNode.left = creatBTree(data, 2 * index + 1) # [1, 3, 7, 15, ...]
        pNode.right = creatBTree(data, 2 * index + 2) # [2, 5, 12, 25, ...]
    return pNode 

class Solution_fail:
    
    def __init__(self):
        self.ans = 0
        self.ans_opt = []
        
    def maxDepth_opt(self, root: TreeNode) -> int:        
        
        if root == None:
            return 0
        if (root.left == None) and (root.right == None):
                self.ans+=1
                self.ans_opt.append(self.ans)
                return 0
        if root.left != None and root.right != None:
            #self.ans+=1
            self.maxDepth_opt(root.left)
            self.maxDepth_opt(root.right)
        if root.left and root.right == None:
                #self.ans+=1
                self.maxDepth_opt( root.left)
        if root.right and root.left == None:    
                #self.ans+=1
                self.maxDepth_opt(root.right)

    
    def maxDepth(self, root: TreeNode) -> int:
        self.maxDepth_opt(root)
        return self.ans

class Solution_1(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            queue = []
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            level = queue
            
        return depth
def main():

    a = Solution()
    root = [3,9,20,None,None,15,7]
    root1 = [1,2,3,4,None,None,5]  
    print(a.maxDepth(creatBTree(root1,0)))
    print(a.ans_opt)

if __name__ == "__main__":
    main()