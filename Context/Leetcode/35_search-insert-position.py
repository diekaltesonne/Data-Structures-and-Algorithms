class Solution:
    def searchInsert(self, nums, target: int) -> int:
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
            else:
                if (i == len(nums)-1):
                        return i+1
        

def main():
    a = Solution()
    print(a.searchInsert(nums = [1,3,5,6], target = 5))
    print(a.searchInsert(nums = [1,3,5,6], target = 2))
    print(a.searchInsert(nums = [1,3,5,6], target = 7))
    print(a.searchInsert(nums = [1,3,5,6], target = 0))
    print(a.searchInsert(nums = [1], target = 0))

if __name__ == "__main__":
    main()