class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r =  0, len(heights) -1
        maximum = 0
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            print('height', height)

            cur_area  = width * height
            print('width:', width)
            print('height:', height)
            print(cur_area)
            if cur_area > maximum:
                maximum = cur_area
                print('maximum,', cur_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r-=1
                
            
        return maximum
                    