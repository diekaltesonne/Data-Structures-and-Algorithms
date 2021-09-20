# https://www.hackerrank.com/challenges/the-minion-game/problem

def sub_algo_2(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

def sub_algo(word,stut,substr):
    stut[substr]=sub_algo_2(word, substr)
    print(stut[substr])
    if  word.find(substr)+len(substr)>(len(word)-1):
        return stut
    else:
        new_substr = substr+word[word.find(substr)+len(substr)]
        return sub_algo(word,stut,new_substr)
       

def stuart_algo(word,dictionary):
    stut = {}
    for letter in word:
        if letter not in dictionary:
            if letter not in stut:
                sub_algo(word,stut,letter)
    return sum(list(stut.values()))
    
def kevin_algo(word,dictionary):
    # Vowels are only defined as AEIOU . In this problem, Y is not considered a vowel.
    kevin = {}
    for letter in word:
        if letter in dictionary:
            sub_algo(word,kevin,letter)
    return sum(list(kevin.values()))

def minion_game_0(word):
    dictionary = {"A","E","I","O","U"}
    stut = {}
    kev = {}
    a = stuart_algo(word,dictionary)
    print("play")
    b = kevin_algo(word,dictionary)
    print("Stuart",a)
    print("Kevin",b)
    if(a>b):
        print("Stuart",a)
    if(a<b):
        print("Kevin",b)

def minion_game(string):
    vowel =['A','E','I','O','U']
    S=0
    K=0
    for i in range(len(string)):
        if string[i] in vowel:
            K+= len(string)-i
        else:
            S+=len(string)-i
    if S>K:
        print("Stuart"+" "+ "%d" % S)
    elif K>S:
        print("Kevin"+" "+'%d' % K)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
