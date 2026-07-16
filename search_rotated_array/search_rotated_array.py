class Solution:
    def search(self, nums: [int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = left + (right-left)//2
        sol = -1
        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[right] == target:
                return right
            elif nums[left] == target:
                return left
            if nums[left] <= nums[mid]:
                if target > nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            mid = left + (right-left)//2
        return sol
