class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rest = []
        for idx, a in enumerate(nums):
            if idx > 0 and a == nums[idx -1]:
                continue
            
            l, r = idx +1, len(nums)-1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -=1
                elif threesum < 0:
                    l += 1
                else:
                    rest.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] ==  nums[l-1]:
                        l += 1
        return rest
