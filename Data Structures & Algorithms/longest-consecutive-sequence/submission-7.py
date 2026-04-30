class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force
        if len(nums) == 0:
            return 0
        
        nums.sort()
        current_streak = 1
        longest_streak = 1

        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                continue
            
            if nums[i] == nums[i -1] +1:
                current_streak +=1
            else:
                longest_streak = max(current_streak, longest_streak)
                current_streak = 1

        res = max(current_streak, longest_streak)
        return res