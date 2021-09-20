# python3

class HashTable:
    
    def __init__(self,number_of_backets) -> None:
        self.bucket_count = number_of_backets
        self.list_of_buckets = [[]] * number_of_backets
        
    # def poly_hash(self, str:str, p = 1000000007, x = 263) -> int: 
    #     hash = 0
    #     for i in range(len(str)-1,0,-1):
    #         hash = (hash * x + ord(str[i])) % p
    #     return hash

    def poly_hash(self, s):
        _multiplier = 263
        _prime = 1000000007
        ans = 0
        for c in reversed(s):
            ans = (ans * _multiplier + ord(c)) % _prime
        print(ans % self.bucket_count)
        return ans % self.bucket_count
    
    def add(self, str:str) -> None:
        if self.find(str) == False:
            self.list_of_buckets[self.poly_hash(str)].append(str)
        

    def delete(self, str:str) -> None:
        #print(self.poly_hash(str))
        #print(self.list_of_buckets[self.poly_hash(str)])
        if self.find(str):
            self.list_of_buckets[self.poly_hash(str)].remove(str)
        #print(self.list_of_buckets[self.poly_hash(str)])
        

    def find(self, str:str) -> str:
        if str in self.list_of_buckets[self.poly_hash(str)]:
            return True
        return False

    def check(self, i:int) -> str:
        print(self.list_of_buckets)
        return reversed(self.list_of_buckets[i])
        

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    result = []
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []

        self.hash_table = HashTable(bucket_count)

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count
    
    def write_responses(self):
        print('\n'.join(self.result))

    def write_search_result(self, was_found):
        self.result.append('yes' if was_found else 'no')

    def write_chain(self, chain):
        self.result.append(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            # self.write_chain(cur for cur in reversed(self.elems)
            #             if self._hash_func(cur) == query.ind)
            self.write_chain(self.hash_table.check(query.ind))
        else:
            if query.type == 'find':
                self.write_search_result(self.hash_table.find(query.s))
            elif query.type == 'add':
                self.hash_table.add(query.s)
            elif query.type == 'del':
                self.hash_table.delete(query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())
        self.write_responses()

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
