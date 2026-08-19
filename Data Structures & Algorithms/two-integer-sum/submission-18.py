class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        l = 0
        while l < len(nums):
            #print(f'current l:{l}')
            for r in range(l+1, len(nums)):
                #print(f'current r:{r}')
                if nums[l] + nums[r] == target:
                    #print('yes')
                    result.append(l)
                    result.append(r)
                    return result
            l += 1
            #print(f'increment l to {l}')
        return []
            

        