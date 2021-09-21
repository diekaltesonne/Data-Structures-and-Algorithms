#Uses python3
import sys
import math
import queue
import heapq

def module(x1,y1,x2,y2):
        return math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))

def distance(lfp: list ,path: list, x, y):
    result = 0
    for i in path:
        result += module(x,y,lfp[i][0],lfp[i][1])
        x,y = lfp[i][0],lfp[i][1]
    return result

def minimum_distance(x, y):
    cost = []
    parent = []
    lfp =[]
    for i, _ in enumerate(x):
        cost.append(math.inf)
        parent.append(0)
        lfp.append([x[i],y[i]])
    H = queue.PriorityQueue()
    H.put([0,0])
    cost[0] = 0
    mstSet = set()
    b = []
    
    while not H.empty():
        u = H.get()[1]
        mstSet.add(u)
        b.append(u)
        for i, cord in enumerate(lfp):
            w = module(cord[0],cord[1],lfp[u][0],lfp[u][1])
            if i not in mstSet and cost[i] > w:
                cost[i] = w
                parent[i] = u
                H.put([cost[i],i])
    
    print(mstSet)
    print(b)
    print(parent)
    return distance(lfp, b, lfp[b[0]][0],lfp[b[0]][1])
    #return distance(lfp, parent, lfp[parent[0]][0],lfp[parent[0]][1])



def extract_min(H: list, mstSet):
    min = math.inf
    for v in range(len(H)):
        if H[v] < min:
            min = H[v]
            min_index = v
    H[min_index] = math.inf
    return min_index

def change_priority(H: list ,i,cost):
    H[i] = cost
def check(H: list):
    return len(set(H)) == 1


def minimum_distance2(x, y):
    b = []
    cost = []
    parent = []
    lfp =[]

    for i, _ in enumerate(x):
        cost.append(math.inf)
        parent.append(0)
        lfp.append([x[i],y[i]])

    H = [math.inf] * n
    H[0] = 0
    cost[0] = 0
    mstSet = set()
    
    while True:
        if check(H):
             break
        u = extract_min(H,mstSet)
        mstSet.add(u)
        b.append(u)
        for i, cord in enumerate(lfp):
            w = module(lfp[u][0],lfp[u][1], cord[0],cord[1])
            #if i not in mstSet and cost[i] > w:
            if cost[i] > w:
                cost[i] = w
                parent[i] = u
                change_priority(H, i, cost[i])
    print(mstSet)
    print(b)
    print(parent)
    return distance(lfp, b, lfp[b[0]][0],lfp[b[0]][1])
    #return distance(lfp, parent, lfp[parent[0]][0],lfp[parent[0]][1])
#
#  I was trying to Prim's pseudo code from lecture, yet by two types of realisation 
# of priority queue (by cost).
# regular list: set q=list(code)
# In a loop, ExtractMin by extracting "u" the index of min(q) then reset q[u] to inf,  
# add u to tree. 
# Next do a loop of all nodes that are not in the tree yet, 
# where cost is replaced by a smaller distance to u. This passed.

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
