class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_count = 1, 0

        for num in nums:
            if num:
                prod *= num
            else:
                zero_count += 1
        if zero_count > 1:
            return [0]*len(nums)
        
        res = [0] * len(nums)
        for idx, val  in enumerate(nums):
            if zero_count:
                res[idx] = 0 if val else prod
            else:
                res[idx] = prod// val
        return res
