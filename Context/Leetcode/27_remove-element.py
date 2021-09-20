class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while nums:
            nums.remove(val)
            if nums.count(val) == 0:
                break
        return len(nums)