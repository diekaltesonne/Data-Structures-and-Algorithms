from typing import List
# - [How to Convert a Python String to int](https://realpython.com/convert-python-string-to-int/)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(format((int(a,base=2))+(int(b,base=2)),'b'))
def main():
    a = Solution()
    print(a.addBinary(a = "11", b = "1"))
    print(a.addBinary(a = "1010", b = "1011"))



if __name__ == "__main__":
    main()