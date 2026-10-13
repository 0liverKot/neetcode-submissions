class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        x = 0
        y = len(numbers) - 1

        while numbers[x] + numbers[y] != target:
            if numbers[x] + numbers[y] > target:
                y -= 1
        
            else:
                x += 1
        return [x + 1, y + 1]





