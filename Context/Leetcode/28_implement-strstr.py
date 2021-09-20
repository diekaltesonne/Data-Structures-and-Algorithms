class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "": return 0
        if len(needle) > len(haystack): return -1
        
        k = 0
        j = 0
        for i in range(len(haystack)):
            
            if haystack[i] == needle[j]:
                if j == 0:
                    k = i
                if len(needle) != 1:
                    j += 1
            else:
                j = 0
                k = 0
            
            if j  == len(needle) - 1:
                if needle[0] == haystack[k]:
                    return k
                    
        return -1


def main():
    a = Solution()
    print(a.strStr("hello","ll"))
    print(a.strStr("aaaaa","bba"))
    print(a.strStr("",""))
    print(a.strStr("abc","c"))
    print(a.strStr("aaa","aaaa"))
    print(a.strStr("mississippi","issip"))

if __name__ == "__main__":
    main()