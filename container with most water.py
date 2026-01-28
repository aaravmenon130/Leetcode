#https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        n = len(height)
        l = 0
        r = n - 1
        while l != r:
            if height[l] < height[r]:
                vol = height[l] * (r - l)
                l += 1
            else:
                vol = height[r] * (r - l)
                r -= 1            
            if vol > max_vol:
                max_vol = vol
        return max_vol
