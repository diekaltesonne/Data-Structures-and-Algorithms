# python3


def build_heap(data):
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps

def _maxheapify(array,n,i, swaps):
    left = 2*i+1
    right = 2*i + 2

    if left<n and array[left]>array[i]:
        largest = left
    else:H
        largest = i
    if right<n and array[right]>array[largest]:
        largest = right
    if largest != i:
        swaps.append((array[i], array[largest]))
        array[i], array[largest] = array[largest], array[i]
        _maxheapify(array,n,largest, swaps)

def _minheapify(array,n,i,swaps):
        l=2*i+1
        r=2*i+2
        if l<n and array[l]<array[i]:
            smallest = l
        else:
            smallest = i
        if r < n and array[r]<array[smallest]:
            smallest = r
        if (smallest != i):
            swaps.append((array[smallest], array[i]))
            array[smallest], array[i] = array[i], array[smallest]
            _minheapify(array, n, smallest,swaps)

def build_heap_efficient(data):   
    swaps = []
    n = len(data)
    for i in range(len(data)//2-1,-1,-1):
        _maxheapify(data,n,i, swaps)
    return swaps

def main():

    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap_efficient(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    print(data)


if __name__ == "__main__":
    main()
