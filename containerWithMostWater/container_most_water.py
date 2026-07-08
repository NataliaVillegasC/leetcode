
""" O(n^2) solution for the container with most water problem
    Does NOT pass test 54 exceed time limit
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for left in range(len(height)):
            for right in range(len(height)):
                if left != right:
                    current_height = min(height[left], height[right])
                    current_area = current_height * (right - left)
                    if max_area < current_area:
                        max_area = current_area
        return max_area"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            current_height = min(height[left], height[right])
            current_area = current_height * (right - left)
            if max_area < current_area:
                max_area = current_area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
    
height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
print(solution.maxArea(height))
