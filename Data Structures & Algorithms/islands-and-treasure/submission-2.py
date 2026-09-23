class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        maxHeight = len(grid) 
        maxWidth = len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] 

        q = deque()

        for i in range(len(grid)): 
            for j in range(len(grid[0])):
                if grid[i][j] == 0: 
                    q.append((i, j))
                    
        while q: 
            
            node = q.popleft()
            row = node[0]
            col = node[1]
            # create enque candidates 
            for dy, dx in directions: 
                nrow = row + dy 
                ncol = col + dx
                if 0 <= nrow < maxHeight and 0 <= ncol < maxWidth and grid[nrow][ncol] == (2 ** 31 - 1): 
                    grid[nrow][ncol] = grid[row][col] + 1
                    q.append((nrow, ncol))
                

