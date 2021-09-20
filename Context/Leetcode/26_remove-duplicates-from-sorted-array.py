class Solution:
    def removeDuplicates(self, nums) -> int:
        prev = None
        i = 0
        while nums:
            if prev == nums[i]:
                nums.pop(i-1)
            else:
                prev = nums[i]
                i+=1
            if i == len(nums):
                break
            
        return len(nums)