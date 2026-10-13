class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        columns = [[] for i in range(9)]

        for row in board:
            
            clean_row = [i for i in row if i != "."]
            if len(set(clean_row)) != len(clean_row):
                return False

            for i in range(len(row)):
                columns[i].append(row[i])

        for column in columns:
            clean_column = [i for i in column if i != "."]
            if len(set(clean_column)) != len(clean_column):
                return False
        

        centers = [
            [1,1], [4,1], [7,1],
            [1,4], [4,4], [7,4],
            [1,7], [4,7], [7,7]
        ]

        for center in centers:
            square = []
            for i in range(center[0] - 1, center[0] + 2):
                for j in range(center[1] - 1, center[1] + 2):
                    if board[i][j] != ".":
                        square.append(board[i][j])
            
            if len(set(square)) != len(square):
                return False

        return True