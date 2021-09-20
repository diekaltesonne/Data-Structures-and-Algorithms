# python3

import sys

def rabinKarp(s : str, w : str):
	answer = [] 
	n = len(s)
	m = len(w)
	r = 2000000
	p = 20
	hashS = hash(s[0..m - 1])
	hashW = hash(w[0..m - 1])
	for i in range(0,n - m,1):
		if hashS == hashW:
			answer.append(i)
		hashS = (p * hashS - pow(p,m) * hash(s[i]) +hash(s[i + m]))%r  # r — некоторое большое число, p — некоторое просто число
	return answer

# class Solver:
# 	def __init__(self, s):
# 		self.s = s
# 	def ask(self, a, b, l):
#		return s[a:a+l] == s[b:b+l]

s = sys.stdin.readline()
q = int(sys.stdin.readline())
#solver = Solver(s)
# for i in range(q):
# 	a, b, l = map(int, sys.stdin.readline().split())
print(rabinKarp(q, s))
