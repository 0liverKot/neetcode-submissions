class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left = 0
        right = len(matrix) - 1
        m = None
        n = None

        while left <= right:

            mid_row = left + (right - left) // 2
            if target >= matrix[mid_row][0] and target <= matrix[mid_row][-1]:
                m = mid_row
                break

            if target > matrix[mid_row][-1]:
                left = mid_row + 1
            
            if target < matrix[mid_row][0]:
                right = mid_row - 1
        
        if m is None:
            return False

        left = 0
        right = len(matrix[0]) - 1

        while left <= right:

            mid_column = left + (right - left) // 2
            if target == matrix[m][mid_column]:
                return True

            if target > matrix[m][mid_column]:
                left = mid_column + 1

            if target < matrix[m][mid_column]:
                right = mid_column - 1

        return False