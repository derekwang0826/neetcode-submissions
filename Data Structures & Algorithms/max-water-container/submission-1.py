class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        current_max = 0
        while left != right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            current_max = max(current_max, area)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return current_max