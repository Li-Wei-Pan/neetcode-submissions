class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force sol1 attempt

        n = len(nums)
        result = [0] * n

        for i in range(n):
            product = 1
            for j in range(n):
                if i == j:
                    continue
                product *= nums[j]
            result[i] = product
        return result