class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left <= right:
            mid = (right + left) // 2
            
            if mid > len(nums) - 1:
                break

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1