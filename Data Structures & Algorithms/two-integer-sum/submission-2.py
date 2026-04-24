class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range (len(nums)):
            difference = target - nums[i]
            if difference in nums:
                j = nums.index(difference)
                if i != j and nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    break


        
        
        result = sorted(result)
        return result
