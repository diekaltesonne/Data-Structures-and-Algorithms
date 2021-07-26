# python3
class PhoneBook:
    phone_book = {}
    
    def __init__(self) -> None:
        pass

    def add(self, name, number):
        self.phone_book[number] = name

    def delete(self, number):
        if self.phone_book.get(number):
            self.phone_book.pop(number)
    
    def find(self,number):
        if self.phone_book.get(number):
            return self.phone_book[number]
        else:
            return 'not found'

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    phone_book = PhoneBook()
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            phone_book.add(cur_query.name, cur_query.number)
        elif cur_query.type == 'del':
            phone_book.delete(cur_query.number)
        else:
            result.append(phone_book.find(cur_query.number))
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

