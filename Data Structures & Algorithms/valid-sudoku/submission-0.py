class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                grid_idx = (row // 3) * 3 + (col // 3)
                if num  == ".":
                    continue
                if num in rows[row] or num in cols[col] or num in grid[grid_idx]:
                    return False
                rows[row].add(num)
                cols[col].add(num)
                grid[grid_idx].add(num)
        return True

    # idx
#            0       1       2
# row:0    [0 1 2] [3 4 5] [6 7 8]
# row: 1   [0 1 2] [3 4 5] [6 7 8]
# row: 2   [0 1 2] [3 4 5] [6 7 8]
#            3       4       5
# row: 3   [0 1 2] [3 4 5] [6 7 8]
# row: 4   [0 1 2] [3 4 5] [6 7 8]
# row: 5   [0 1 2] [3 4 5] [6 7 8]
#            6       7       8
# row: 6   [0 1 2] [3 4 5] [6 7 8]
# row: 7   [0 1 2] [3 4 5] [6 7 8]
# row: 8   [0 1 2] [3 4 5] [6 7 8]
