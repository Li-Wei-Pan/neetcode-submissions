class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        for i in range(len(nums)):
            current_product = 1
            tem_lst = nums.copy()
            tem_lst.remove(nums[i])
            for j in tem_lst:
                current_product *= j
            output.append(current_product)
        return output