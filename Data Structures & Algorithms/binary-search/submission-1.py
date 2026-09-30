class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # add index for each num
        
        l, r = 0 , len(nums)-1
        while l <= r:
            pivot = l + (r - l) // 2 
            # print('cur_pivot', pivot)
            if nums[pivot] < target:
                l = pivot +1
            elif nums[pivot] > target:
                r =  pivot -1
            else:
                return pivot
        return -1