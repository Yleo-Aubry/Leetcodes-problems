class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        max_water = 0
        
        while l < r:
            min_height = min(height[l], height[r])
            base = r - l
            
            current_area = min_height * base
            max_water = max(max_water, current_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_water
