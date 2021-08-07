# [A program to check if a binary tree is BST or not](https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/)
import sys, threading
sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeChecker():
  
  def __init__(self,tree) -> None:
       self.tree = tree
  
  def isBSTUtil(self, i, mini, maxi):     
      if i == -1:
          return True
      # False if this node violates min/max constraint
      if self.tree[i][0] < mini or self.tree[i][0] > maxi:
          return False
      # Otherwise check the subtrees recursively
      # tightening the min or max constraint
      return (self.isBSTUtil(self.tree[i][1],mini, self.tree[i][0] -1 ) and
            self.isBSTUtil(self.tree[i][2], self.tree[i][0], maxi))

  def isBST(self):
    if len(self.tree) == 0:
      return True
    return (self.isBSTUtil(0, -4294967296, 4294967296))

def IsBinarySearchTree(tree):
   return TreeChecker(tree).isBST()

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
