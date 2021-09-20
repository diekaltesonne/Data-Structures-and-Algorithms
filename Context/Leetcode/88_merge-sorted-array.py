from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0
        nums = []
        for i in range(0,m,1):
            nums.append(nums1[i])
        for j in range(0,n,1):
            nums.append(nums2[j])
        nums.sort()
        nums1.clear()
        nums1.extend(nums)
                         


def main():
    a = Solution()
    nums1 = [1,2,3,0,0,0] 
    m = 3
    nums2 = [2,5,6]
    n = 3
    a.merge(nums1,m,nums2,n)
    print(nums1)



if __name__ == "__main__":
    main()