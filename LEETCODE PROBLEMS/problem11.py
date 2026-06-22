class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(height) - 1

        while l < r :
            max_area = max(max_area, (r- l) * min(height[l], height[r]))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
#Example 1:
#Input: height = [1,8,6,2,5,4,8,3,7]
#Output: 49