class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        previous_number = None

        for i in range(len(nums) - 2):
            number = nums[i]

            if number == previous_number:
                continue
            previous_number = number

            if number > 0:
                break

            start = i + 1
            end = len(nums) - 1

            while True:
                if number + nums[start] + nums[end] == 0:
                    res.append([number, nums[start], nums[end]])    

                    end -= 1
                    while nums[end] == nums[end + 1]:
                        end -= 1
                        if end - start < 2:
                            break 

                if end - start <= 1:
                    break

                if number + nums[start] + nums[end] > 0:
                    end -= 1

                else: 
                    start += 1
                            
        return res