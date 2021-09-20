# https://www.hackerrank.com/challenges/compress-the-string/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

class groupby(object):    
    def __init__(self, iterable, key=None):
        if key is None:
            key = lambda x: x
        self.keyfunc = key
        self.it = iter(iterable)
        self.tgtkey = self.currkey = self.currvalue = object()

    def next(self):
        while self.currkey == self.tgtkey:
            self.currvalue = next(self.it)    # Exit on StopIteration
            self.currkey = self.keyfunc(self.currvalue)
        self.tgtkey = self.currkey
        return (self.currkey, self._grouper(self.tgtkey))

    def __iter__(self):
        return self
    
    def _grouper(self, tgtkey):
        while self.currkey == tgtkey:
            yield self.currvalue
            self.currvalue = next(self.it)    # Exit on StopIteration
            self.currkey = self.keyfunc(self.currvalue)


def compress_the_string(st):
    for k in groupby('123'):
        str += "(%a,%b)".format(list(g).count,k) 
    return str


if __name__ == '__main__':
    a=input()
    s=''
    for i in range(0,len(a)):
        if i!=0:
            if a[i]==a[i-1]:  
                continue
        p=0
        for j in range(i,len(a)):
            if a[i]==a[j]:
                p+=1
            else:
                break
        s+='('+str(p)+', '+a[i]+')'+' '
    print(s)
