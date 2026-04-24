class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for ind1 in range(len(nums)-1):
            pivot = nums[ind1]
            print('ind1:', ind1)
            for j in range(ind1 +1, len(nums)):
                print("j:", j)
                if pivot == nums[j]:
                    return True
              
        return False
            
        