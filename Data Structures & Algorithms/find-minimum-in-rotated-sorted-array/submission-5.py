class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        left = 0 
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[left] < nums[right]:
                return min(res, nums[left])

            res = min(res, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return res