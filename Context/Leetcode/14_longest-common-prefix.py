class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        vow = ("a","e","o","i","u","y")
        a = ""
        b = []
        for i in strs:
            for j in range(len(i)):
                if i[j] in vow:
                    b.append(a)
                    a = ""
                    break
                else:
                    a = a +i[j]

        if len(b)== 0:
            return ""
        
        ans =  max(b, key=len)
        
        if len(ans) <= 1:
            return ""
        else:
            return ans
        