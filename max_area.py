class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        maxarea = 0
        while (left < right):
            cwidth = right-left
            cheight = min(height[right], height[left])
            maxarea = max(maxarea, cwidth * cheight)

            if (height[right] > height[left]):
                left += 1
            else :
                right -= 1
        
        return maxarea