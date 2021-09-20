from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans =  s.split(" ")
        for i in range(len(ans)-1,-1,-1):
            if ans[i] != '' :
                return len(ans[i])
            

def main():
    a = Solution()
    print(a.lengthOfLastWord(s = "Hello World"))
    print(a.lengthOfLastWord(s = "a "))


if __name__ == "__main__":
    main()