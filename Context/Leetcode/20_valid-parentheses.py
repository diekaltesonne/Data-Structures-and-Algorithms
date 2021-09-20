class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        for i in s:
            if i == "{" or i == "[" or i == "(":
                a.append(i)
                continue
            if len(a) == 0 :
                    return False
            if a[-1] == "{" and i == "}":
                    a.pop()
                    continue
            if a[-1] == "[" and i == "]":
                    a.pop()
                    continue
            if a[-1] == "(" and i == ")":
                    a.pop()
                    continue
            return False
        
        if len(a) != 0:
            return False
        
        return True

a = Solution()

print(a.isValid("(])"))

            