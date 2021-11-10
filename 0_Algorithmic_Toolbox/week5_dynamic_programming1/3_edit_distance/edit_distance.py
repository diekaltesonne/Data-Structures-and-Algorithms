# Uses python3
def edit_distance(s, t):
    len_s = len(s) + 1
    len_t = len(t) + 1
    D = [[x] + [0] * (len_t - 1) for x in range(len_s)]
    D[0] = [x for x in range(len_t)]
    for i in range(1,len_s):
        for j in range(1,len_t): 
            if s[i - 1] == t[j - 1]:
                D[i][j] = D[i - 1][j - 1]
            else:
                D[i][j] = min(D[i][j-1] ,D[i-1][j],D[i-1][j-1])+1
    return D[-1][-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))