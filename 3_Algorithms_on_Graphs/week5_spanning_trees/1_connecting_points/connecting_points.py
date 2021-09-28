#Uses python3
# Prim(G)
#   for all u ∈ V:
#     cost[u] ← ∞, parent[u] ← nil
#   pick any initial vertex u0
#   cost[u0] ← 0
#   PrioQ ← MakeQueue(V) {priority is cost}
#   while PrioQ is not empty:
#     v ← ExtractMin(PrioQ)
#     for all {v, z} ∈ E:
#       if z ∈ PrioQ and cost[z] > w(v, z):
#         cost[z] ← w(v, z)
#         parent[z] ← v
#         ChangePriority(PrioQ, z, cost[z])

#  I was trying to Prim's pseudo code from lecture, yet by two types of realisation 
# of priority queue (by cost).
# regular list: set q=list(code)
# In a loop, ExtractMin by extracting "u" the index of min(q) then reset q[u] to inf,  
# add u to tree. 
# Next do a loop of all nodes that are not in the tree yet, 
# where cost is replaced by a smaller distance to u. This passed.
import sys
import math
import queue
import heapq

def module(x1,y1,x2,y2):
        return math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))

def change_priority(H: list ,i,cost):
    for j in H:
        if j[1]==i:
            j[0] = cost
            heapq.heapify(H)
            return 0
    H.append([cost,i])

def check(H: list,i):
    for j in H:
        if j[1] == i:
            return True
    return False
   
def minimum_distance3(x, y):
    cost = []
    parent = []
    lfp =[]
    H = []
    min_l = 0
    for i, _ in enumerate(x):
        cost.append(math.inf)
        lfp.append([x[i],y[i]])
        H.append([math.inf,i])
    
    H[0][0] = 0
    cost[0] = 0

    while len(H) != 0:
        heapq.heapify(H)
        u = heapq.heappop(H)
        min_l += u[0]
        u = u[1]
        parent.append(u)
        for i, cord in enumerate(lfp):
            if check(H, i): 
                w = module(lfp[u][0],lfp[u][1], cord[0],cord[1])
                if cost[i] > w :
                    cost[i] = w
                    change_priority(H, i, cost[i])
    return min_l

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance3(x, y)))
