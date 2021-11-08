# Uses python3
import sys

def get_change(m):
    min_num_coins = [0]*(m+1)
    coins = [1, 3, 4]
    for i in range(1,len(min_num_coins),1):
        min_num_coins[i] = 100000
        for j in range(len(coins)):
            if i >= coins[j]:
                num_coins = min_num_coins[i - coins[j]] + 1
                if num_coins < min_num_coins[i]:
                    min_num_coins[i] = num_coins
    return min_num_coins[-1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))