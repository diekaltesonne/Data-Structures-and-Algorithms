#!/usr/bin/python3
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  ans = False
  if len(tree) == 0:
    return True
  for i in tree:
    if ((i[1] < i[0]) or (i[1] == -1)) and ((i[0] <= i[2]) or (i[2] == -1)):
      ans = True
    else:
      ans = False
      break
  return ans


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
