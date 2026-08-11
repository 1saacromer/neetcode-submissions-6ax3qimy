class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        grid = defaultdict(list)

        for row in range(9): 
            for col in range(9): 
                
                val = board[row][col]

                if not val.isdigit(): 
                    continue

                if val in rows[row]:
                    return False
                rows[row].append(val)

                if val in cols[col]:
                    return False
                cols[col].append(val)
                
                idx = (row // 3) * 3 + col // 3
                if val in grid[idx]:
                    return False
                grid[idx].append(val)

                print(rows, cols, grid)

        return True 