class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        current_max = 0
        height_left = heights[left]
        height_right = heights[right]
        while left < right:
            if height_left < heights[left]:
                height_left = heights[left]
            if height_right < heights[right]:
                height_right = heights[right]
            width = right - left
            height = min(height_left, height_right)
            area = width * height
            current_max = max(current_max, area)
            if height_left > height_right:
                right -= 1
            else:
                left += 1
        return current_max