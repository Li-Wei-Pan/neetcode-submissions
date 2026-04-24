class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums1 = nums.copy()
        nums1 = set(nums1)
        return True if len(nums1) < len(nums) else False
        