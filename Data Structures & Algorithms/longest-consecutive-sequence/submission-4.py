class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        
        res = 0
        cur = 0

        for num in nums:
            if num - 1 not in num_set:

                for i in range(len(num_set)):
                    
                    if num + i in num_set:
                        cur += 1
                        if cur > res:
                            res = cur
                    else:
                        break
                cur = 0

        return res