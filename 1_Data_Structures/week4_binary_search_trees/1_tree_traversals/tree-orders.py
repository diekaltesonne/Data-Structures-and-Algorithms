# python3
# [Дерево поиска, наивная реализация](https://neerc.ifmo.ru/wiki/index.php?title=%D0%94%D0%B5%D1%80%D0%B5%D0%B2%D0%BE_%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0,_%D0%BD%D0%B0%D0%B8%D0%B2%D0%BD%D0%B0%D1%8F_%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F)
import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def _inOrder(self,i):
    if i != -1:
      self._inOrder(self.left[i]) 
      self.result.append(self.key[i]) 
      self._inOrder(self.right[i])
    else:
        return 0

  def inOrder(self):
    self.result = []
    self._inOrder(0)
    return self.result

  def _preOrder(self,i):
    if i != -1:
      self.result.append(self.key[i]) 
      self._preOrder(self.left[i]) 
      self._preOrder(self.right[i])
    else:
        return 0
    
  def preOrder(self):
    self.result = []
    self._preOrder(0)             
    return self.result

  def _postOrder(self,i):
    if i != -1: 
      self._postOrder(self.left[i]) 
      self._postOrder(self.right[i])
      self.result.append(self.key[i])
    else:
        return 0
    
  def postOrder(self):
    self.result = []
    self._postOrder(0)
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
